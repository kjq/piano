"""
:mod:`piano.resources.contexts`
-------------------------------

.. autoclass:: App
   :members:
   
.. autoclass:: Service
   :members:

.. autoclass:: Site
   :members:
   
.. autoclass:: Page
   :members:

.. autoclass:: Root
   :members:
         
"""
from beaker.cache import cache_region
from collections import namedtuple
from piano import constants as c
from piano.lib import base as b
from piano.lib import helpers as h
from piano.resources import interfaces as i
from pyramid.security import Allow, Everyone
from zope.interface import implementer
import logging

logger = logging.getLogger(__name__)

SiteItem = namedtuple('Site', ['title', 'slug'], verbose=False)

class Root(b.ContextBase):
    """The root segment is the entry-point into the context tree.  From the
    root it will try to find an application, then the site, then any pages. The
    only exception are services (/services) which can only be accessed from the 
    the root.
    """
    __acl__ = [ (Allow, Everyone, 'view'),
                (Allow, 'group:editors', 'edit') ]

    def __init__(self, request):
        self.request = request

    def __getitem__(self, key):
        # If /services return the service context
        if key == c.SRVC_NAME:
            return Service(key=key, parent=self)
        #Try and return an app context otherwise
        try:
            return self.app(key=key, parent=self)
        except:
            raise KeyError(key)


class Service(b.ContextBase):
    """The service segment (/services) acts as the entry-point for all services
    that are exposed.  Currently, this comprises RESTful services only.
    """
    pass

@implementer(i.IApp)
class App(b.ContextBase):
    """The app segment specifies which 'database' is used for all segments
    following.  At a high-level it represents the application being accessed
    and is the master container for sites and pages.  If the database does not
    exist during an operation it will be created.
    """
    def __getitem__(self, key):
        try:
            return Site.find(key=key, parent=self)
        except:
            raise KeyError(key)

    def list_sites(self):
        """Returns a list of sites under the application.
        """
        #@cache_region('hourly', 'site.list')
        def _list_sites(a):
            doc = self.get_conn(a).SiteDocument.find({}, {'title':1, 'slug':1})
            return list(SiteItem(s['title'], '/'.join([a, s['slug']])) for s in doc)
        #Get the list of available sites
        site_list = _list_sites(self.appname)
        return site_list


class Page(b.ContextBase):
    """The page segment represents an individual page (i.e. home, contact us,
    site map, etc.).  If the page segment extends beyond a single element it 
    will continue to look up pages until a KeyError is raised at which point
    the view is invoked/resolved.
    """
    def __getitem__(self, key):
        try:
            return Page.find(key=key, parent=self)
        except:
            raise KeyError(key)

    @classmethod
    def find(cls, key, parent):
        """Finds a single page by its parent and slug.
        """
        @cache_region('hourly', 'page.find')
        def _find_page(k, p, s, a):
            return parent.get_conn(app=a, site=s).one({'parent': p, 'slug':k})
        #Find the page
        doc = _find_page(key, parent.__name__, parent.sitename, parent.appname)
        return cls(
            key=key,
            parent=parent,
            id=doc['_id'],
            title=doc['title'],
            data=doc['data'],
            slug=doc['slug'],
            origin=doc['parent'],
            views=doc['views'],
            source=str(doc['source']),
            date_created=doc['created'])

    def create(self, data):
        """Creates a new page and associates it to a parent.
        """
        doc = self.get_conn().PageDocument()
        doc['title'] = self.title = data['page']['title']
        doc['slug'] = self.slug = self.__name__ = str(h.urlify(self.title))
        doc['source'] = self.source = str(data['page']['source'])
        doc['parent'] = str(self.__parent__.__name__)
        #Try to import custom models and get doc
        try:
            #Explicitly look for a 'models' module with a 'PageModel' class
            mod = __import__('.'.join([self.source, c.MODEL_PATH]), fromlist=[self.source])
            pdoc = getattr(mod, c.MODEL_NAME)
        except ImportError:
            logger.warn("Cannot import '%s.models' module" % self.source)
        except AttributeError:
            logger.warn("Cannot load '%s.models.PageModel' class" % self.source)
        else:
            #Embed a new document
            doc['data'] = pdoc()
        doc.save()
        return self

    def update(self, data):
        """Update myself with data
        """
        doc = self.get_conn().PageDocument.get_from_id(self.id)
        doc['title'] = self.title = data['page']['title']
        doc['slug'] = self.slug = self.__name__ = str(h.urlify(data['page']['slug']))
        doc['data'] = self.data = data['data']
        doc.save(validate=False)
        return self

@implementer(i.ISite)
class Site(Page):
    """The site segment represents the entry-point into a collection of pages.
    An application can have many sites and each site can have many pages.
    """
    def __getitem__(self, key):
        try:
            return Page.find(key, self)
        except:
            raise KeyError(key)

    @classmethod
    def find(cls, key, parent):
        """Returns a single site by its slug.
        """
        @cache_region('hourly', 'site.find')
        def _find_site(k, a):
            return parent.get_conn(app=a).SiteDocument.one({'slug':k})
        #Find the site
        doc = _find_site(key, parent.__name__)
        return cls(
            key=key,
            parent=parent,
            id=doc['_id'],
            title=doc['title'],
            slug=doc['slug'],
            views=doc['views'],
            date_created=doc['created'])

    def create(self, data, include_default=False):
        """Saves the primary site details and creates a new collection to house 
        the pages in.  It also creates a default (Home) page if needed.
        """
        doc = self.get_conn(app=self.appname).SiteDocument()
        doc['title'] = self.title = data['site']['title']
        doc['slug'] = self.slug = self.__name__ = str(h.urlify(self.title))
        doc.save()
        #Create default (home) page?
        if include_default:
            data = dict(
                page=dict(
                    title=u'Home',
                    source='sample.home'
                )
            )
            page = Page(parent=self)
            page.create(data)
        return self

    def delete(self):
        """Deletes the site and its associated collection.
        """
        db = self.get_conn(app=self.appname)
        db.SiteDocument.get_from_id(self.id).delete()
        db.drop_collection(self.__name__)