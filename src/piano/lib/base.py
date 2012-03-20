"""
:mod:`piano.libs.base`
---------------------

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
    
    @property
    def conn(self):
        """Returns a MongoDB connection.
        """
        return self.request.conn
    
class DocumentBase(Document):
    """ Base (abstract) class for all documents (MongoDB).
    """
    #: Use MongoKit '.' notation
    use_dot_notation = False
    #: Require schemas to be defined up-front
    use_schemaless = False
    #: Validate models.
    skip_validation = False