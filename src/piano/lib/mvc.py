"""
:mod:`piano.libs.mvc`
---------------------

.. autoclass:: PageModel

"""
class PageModel(dict):
    """ PageModel to standardize the dict values used across pages.
    """
    def __init__(self, context, **kwargs):
        #Page specifics
        self['page_id'] = context.id
        self['page_slug'] = context.slug
        self['page_title'] = context.title
        self['page_template'] = getattr(context, 'template', None)
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