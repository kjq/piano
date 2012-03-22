"""Home Page

:mod:`sample.home`
---------------------

"""
from sample.home import models as m
import logging

logger = logging.getLogger(__name__)

# Manually register documents    
try:
    from piano.lib.mongo import conn
    conn.register([m.HomeData])
except:
    pass
else:
    logger.info('Registered Home models')