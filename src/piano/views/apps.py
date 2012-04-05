"""General Views

:mod:`piano.views.apps`
-----------------------

.. autofunction:: dashboard

"""
from piano.resources import contexts as ctx
from pyramid.view import view_config

@view_config(context=ctx.App, renderer='piano.web.templates.app:dashboard.mako')
def dashboard(context, request):
    """Renders a list of sites available to this application.
    """
    page_title = "Dashboard"
    new_site_url = request.resource_url(context, 'new-site')
    # Find list of sites
    site_list = context.find_sites()
    # Respond
    return dict(
        app_title=page_title,
        sites=site_list,
        page_title=page_title,
        new_site_url=new_site_url)