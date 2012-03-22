"""
:mod:`piano.resources.contexts`
-----------------------------

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
        @cache_region('hourly', 'site.list')
        def _list_sites(a):
            data = self.get_conn(a).SiteDocument.find({}, {'title':1, 'slug':1})
            return list(SiteItem(s['title'], '/'.join([a, s['slug']])) for s in data)
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

    @property
    def template(self):
        """Returns the primary view template in the form 
        [app].[module]:[template].mako.
        
        Example: sample.home:main.mako
        """
        return ':'.join([self.source, c.MAIN_TEMPLATE])

    @classmethod
    def find(cls, key, parent):
        """Finds a single page by its parent and slug.
        """
        @cache_region('hourly', 'page.find')
        def _find_page(k, p, s, a):
            return parent.get_conn(app=a, site=s).one({'parent': p, 'slug':k})
        #Find the page
        data = _find_page(key, parent.__name__, parent.sitename, parent.appname)
        return cls(
            key=key,
            parent=parent,
            id=data['_id'],
            title=data['title'],
            data=data['data'],
            slug=data['slug'],
            origin=data['parent'],
            views=data['views'],
            source=str(data['source']),
            date_created=data['created'])

    def save(self):
        """Creates a new page and associates it to a parent.
        """
        data = self.get_conn().PageDocument()
        data['title'] = self.title
        data['slug'] = self.slug
        data['parent'] = str(self.__parent__.__name__)
        data['source'] = str(self.source)
        #Try to import custom models and get doc
        try:
            #Explicitly look for a 'models' module with a 'PageModel' class
            mod = __import__('.'.join([self.source, 'models']), fromlist=[self.source])
            doc = getattr(mod, 'PageModel')
        except ImportError:
            logger.warn("Cannot import '%s.models' module" % self.source)
        except AttributeError:
            logger.warn("Cannot load '%s.models.PageModel' class" % self.source)
        else:
            #Add new document
            data['data'] = doc()
        data.save()
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
        data = _find_site(key, parent.__name__)
        return cls(
            key=key,
            parent=parent,
            id=data['_id'],
            title=data['title'],
            slug=data['slug'],
            views=data['views'],
            date_created=data['created'])

    def save(self, include_default=False):
        """Saves the primary site details and creates a new collection to house 
        the pages in.  It also creates a default (Home) page if needed.
        """
        data = self.get_conn(app=self.appname).SiteDocument()
        data['title'] = self.title
        data['slug'] = self.slug
        data.save()
        #Create default (home) page?
        if include_default:
            Page(
                key='home',
                parent=self,
                title=u'Home',
                slug='home',
                source='sample.home').save()
        return self

    def delete(self):
        """Deletes the site and its associated collection.
        """
        db = self.get_conn(app=self.appname)
        db.SiteDocument.get_from_id(self.id).delete()
        db.drop_collection(self.__name__)