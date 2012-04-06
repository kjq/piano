"""
:mod:`piano.lib.mvc`
---------------------

.. autofunction:: merge

.. autoclass:: PageModel

"""

from piano import constants as c

def merge(source):
    """Merges the data from the source (dict) into a unified dictionary
    consisting of three dictionaries:
    
        - site
        - page
        - data
    """
    # Site data
    site_data = dict((k.replace(c.SITE_PREFIX, ''), v)
                          for k, v in source
                              if k.startswith(c.SITE_PREFIX))
    # Page data
    page_data = dict((k.replace(c.PAGE_PREFIX, ''), v)
                          for k, v in source
                              if k.startswith(c.PAGE_PREFIX))
    # Model data
    page_model = dict((k.replace(c.DATA_PREFIX, ''), v)
                          for k, v in source
                              if k.startswith(c.DATA_PREFIX))
    return dict(
        site=site_data,
        page=page_data,
        data=page_model)

class PageModel(dict):
    """ PageModel to standardize the dict values used across pages.
    """
    def __init__(self, context, **kwargs):
        #Page specifics
        self['page_id'] = context.id
        self['page_slug'] = context.slug
        self['page_title'] = context.title
        self['page_template'] = getattr(context, 'source', None)
        self['page_data'] = getattr(context, 'data', None)
        #Site specifics
        site = context.__site__
        if site is not None:
            self['site_id'] = site.id
            self['site_slug'] = site.slug
            self['site_title'] = site.title
        #Set extra values
        for key in kwargs:
            self[key] = kwargs[key]