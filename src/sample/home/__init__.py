"""Home Page

:mod:`sample.home`
---------------------

"""
from sample.home import models as m

# Manually register documents    
try:
    from piano.lib.mongo import conn
    conn.register([m.HomeData])
except:
    pass