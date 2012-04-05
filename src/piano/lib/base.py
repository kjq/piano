"""
:mod:`piano.libs.base`
----------------------

.. autoclass:: ContextBase
   :members:
   
.. autoclass:: DocumentBase

"""
from piano.resources import interfaces as i
from mongokit import Document
from pyramid.traversal import find_interface, find_root

class ContextBase(dict):
    """ Base (abstract) class for all resources (contexts).
    """
    __name__ = None
    __parent__ = None
    __app__ = None
    __site__ = None

    def __init__(self, key=None, parent=None, **kwargs):
        self.__name__ = key
        self.__parent__ = parent
        # Reference request
        self.request = find_root(self).request
        # Reference app and site
        self.__app__ = find_interface(self, i.IApp)
        self.__site__ = find_interface(self, i.ISite)
        # Assign kwargs to self (used as self.XXX not self['xxx'])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    @property
    def appname(self):
        """Returns the name of the application.  
        """
        return self.__app__.__name__

    @property
    def sitename(self):
        """Returns the name of the site.  
        """
        return self.__site__.__name__

    def get_conn(self, app=None, site=None):
        """Returns a raw MongoDB connection.  If none of the arguments are
        set it will try to configure the connection based on the instances 
        app and site name.  Otherwise, it is up to you to choose the
        database and collection to use.
        """
        mongo_conn = self.request.conn
        # If no app or site, autoconfigure the connection
        if app is None and site is None:
            return mongo_conn[self.appname][self.sitename]
        #If app or site, build up the connection
        if app is not None:
            mongo_conn = mongo_conn[app]
        if site is not None:
            mongo_conn = mongo_conn[site]
        return mongo_conn


class DocumentBase(Document):
    """ Base (abstract) class for all documents (MongoDB).
    """
    #: Use MongoKit '.' notation
    use_dot_notation = False
    #: Require schemas to be defined up-front
    use_schemaless = False
    #: Validate models.
    skip_validation = False
    #: Authorized types.
    authorized_types = Document.authorized_types + [str]