"""
:mod:`piano.views.history`
------------------------

.. autofunction:: piano.views.history.view_diff

.. autofunction:: piano.views.history.view_history

"""
from piano.resources import contexts as ctx
from pyramid.view import view_config

@view_config(name='history', context=ctx.Page, renderer='piano.web.templates.history:list.mako', request_method='GET')
def view_history(context, request):
    """Renders the history for the page and allows for rollbacks.
    """
    version_list = context.find_history()
    return dict(page_title="Page History",
                page_slug=context.__name__,
                versions=version_list)

@view_config(context=ctx.Version, renderer='piano.web.templates.history:diff.mako', request_method='GET')
def view_diff(context, request):
    """Renders the differences between two versions.
    """
    context.compare(1, 4)
    return dict(page_title="Page Compare",
                page_slug=context.__name__)