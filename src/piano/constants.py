"""Application constants.

:mod:`piano.constants`
----------------------
.. autodata:: piano.constants.SRVC_NAME
.. autodata:: piano.constants.MAIN_TEMPLATE
.. autodata:: piano.constants.MONGO_URL
.. autodata:: piano.constants.MONGO_CONN

"""
#: Default service route
SRVC_NAME = 'services'

#: Default template entry-point
MAIN_TEMPLATE = 'main.mako'

#: MongoDB URL key
MONGO_URL = 'mongodb.url'

#: MongoDB connection key
MONGO_CONN = 'mongodb.conn'

#: PageModel class name default
MODEL_NAME = 'PageModel'

#: PageModel package name default
MODEL_PATH =  'models'

#: Page 'view' template name
VIEW_TEMPLATE = 'view.mako'

#: Page 'edit' template name
EDIT_TEMPLATE = 'edit.mako'

#: Page values suffix for field(s)
SITE_PREFIX = 'site_'

#: Page values suffix for field(s)
PAGE_PREFIX = 'page_'

#: Page data values suffix for model field(s)
DATA_PREFIX = 'data_'

