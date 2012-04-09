"""Application constants.

:mod:`piano.constants`
----------------------
.. autodata:: piano.constants.DATA_PREFIX
.. autodata:: piano.constants.EDIT_TEMPLATE
.. autodata:: piano.constants.HISTORY_COLL
.. autodata:: piano.constants.MAIN_TEMPLATE
.. autodata:: piano.constants.MODEL_NAME
.. autodata:: piano.constants.MODEL_PATH
.. autodata:: piano.constants.MONGO_URL
.. autodata:: piano.constants.MONGO_CONN
.. autodata:: piano.constants.PAGE_COLL
.. autodata:: piano.constants.PAGE_PREFIX
.. autodata:: piano.constants.SITE_PREFIX
.. autodata:: piano.constants.SRVC_NAME
.. autodata:: piano.constants.V
.. autodata:: piano.constants.VIEW_TEMPLATE

"""
#: Page data values suffix for model field(s)
DATA_PREFIX = 'data_'

#: Page 'edit' template name
EDIT_TEMPLATE = 'edit.mako'

#: Mongo History collection
HISTORY_COLL = 'history'

#: Default template entry-point
MAIN_TEMPLATE = 'main.mako'

#: PageModel class name default
MODEL_NAME = 'PageModel'

#: PageModel package name default
MODEL_PATH = 'models'

#: MongoDB URL key
MONGO_URL = 'mongodb.url'

#: MongoDB connection key
MONGO_CONN = 'mongodb.conn'

#: Mongo Page collection
PAGES_COLL = 'pages'

#: Page values suffix for field(s)
PAGE_PREFIX = 'page_'

#: Page values suffix for field(s)
SITE_PREFIX = 'site_'

#: Default service route
SRVC_NAME = 'services'

#: Version URL segment
V = 'v'

#: Page 'view' template name
VIEW_TEMPLATE = 'view.mako'


