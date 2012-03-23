"""
:mod:`piano.resources.documents`
--------------------------------

.. autoclass:: SiteDocument
   :members:
   
.. autoclass:: PageDocument
   :members:
   
"""
from piano.lib import base as b
from piano.lib import helpers as h
import datetime
import logging

logger = logging.getLogger(__name__)

class SiteDocument(b.DocumentBase):
    """"Document representation of a site.
    """
    __database__ = None
    __collection__ = 'sites'

    structure = {
        'slug': str,
        'title': unicode,
        'description':unicode,
        'created': datetime.datetime,
        'views': int,
    }
    required_fields = [
        'title',
        'slug',
        'created'
    ]
    default_values = {
        'views': 1,
        'created': h.now()
    }

class PageData(b.DocumentBase):
    """Document for page-level data.  Page-level components need to have a
    module 'models' and a class 'PageModel' which extends this class.
    """
    structure = {}
    
class PageDocument(b.DocumentBase):
    """"Document representation of a page.
    """
    structure = {
        'title':unicode,
        'slug':str,
        'description':unicode,
        'created': datetime.datetime,
        'keywords': list,
        'views': int,
        'source': str,
        'parent': str,
        'data': PageData,
    }
    required_fields = [
        'title',
        'slug',
        'source',
        'parent',
        'created'
    ]
    default_values = {
        'views': 1,
        'title': u'Home',
        'slug': 'home',
        'source': 'sample.home',
        'created': h.now()
    }
    #Use autorefs for embedded data docs
    use_auto_refs = True
    
# Manually register documents    
try:
    from piano.lib.mongo import conn
    conn.register([
        PageDocument, 
        SiteDocument])
except:
    pass
else:
    logging.debug('Registered Mongo documents')
