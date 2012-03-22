"""
:mod:`piano.services.menu`
-------------------------

.. autoclass:: MenuService
   :members:
   
"""
from piano.resources import contexts as ctx
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPInternalServerError
import logging

logger = logging.getLogger(__name__)

@view_defaults(name="menu", context=ctx.Service, xhr=False, renderer='jsonp')
class MenuService(object):
    """A RESTful command that returns child pages of the parent page or site.
    This command assumes the url always starts with the app, then the site,
    and ends with the page (parent of the children to return).  If it is just 
    the site, then the children of the site are returned only.
    """
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.conn = request.conn
        #QueryArgs
        self.url = request.GET['url']
        self.page = request.GET.setdefault('page', '')
        #Prepare site and/or page urls and strip first/last slash
        segments = self.url.strip('/').split('/')
        self.app = segments[0]
        self.site = segments[1]
        if self.page == '':
            self.parent = self.site
            self.page = None
        else:
            self.parent = self.page
        
    @view_config(request_method='GET')
    def get(self):
        """Returns a dictionary of pages with links.
        
        **Site**: /services/menu?url=/my-site
            - Returns all children for my-site
            
        **Page**: /services/menu?url=/my-site&page=home
            - Returns all children for my-site/home
        """
        try:
            return self._children(self.parent, self.site, self.app)
        except:
            return HTTPInternalServerError("Request did not execute properly.")
    
    def _children(self, parent, site, app):
        coll = self.conn[app][site]
        #Find children of parent then all child in that list
        children = coll.find({'parent': parent}, {'slug':1, 'title':1})
        #Lamba to resolve paths
        r = lambda c: '/'.join([self.url, c])
        #Build children for menu
        return [dict(title=child['title'],
                     slug=child['slug'],
                     url= r(child['slug'])) for child in children]
        