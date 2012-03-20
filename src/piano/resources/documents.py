"""
:mod:`piano.resources.documents`
-------------------------------

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
