"""
:mod:`piano.views.sites`
------------------------

.. autofunction:: piano.views.sites.view_site

.. autofunction:: piano.views.sites.new_site

.. autofunction:: piano.views.sites.delete_site

"""
from piano.lib import mvc
from piano.resources import contexts as ctx
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

@view_config(context=ctx.Site, renderer='piano.web.templates.site:view.mako', request_method='GET')
def view_site(context, request):
    """Main view of the site.
    """
    new_page_url = request.resource_url(context, 'new-page')
    # Respond
    return mvc.PageModel(
        context,
        page_views=context.views,
        page_created=context.date_created,
        new_page_url=new_page_url)

@view_config(name='new-site', context=ctx.App, renderer='piano.web.templates.site:new.mako', request_method='GET')
@view_config(name='new-site', context=ctx.App, request_method='POST')
def new_site(context, request):
    """Add a new site.
    """
    # Handle submission
    if 'form.submitted' in request.params:
        data = mvc.merge(request.POST.items())
        site = ctx.Site(parent=context)
        site.create(data, include_default=True)
        return HTTPFound(location=request.resource_url(context, site.__name__))
    new_site_url = request.resource_url(context, 'new-site')
    # Respond
    return dict(
        page_title="New Site",
        new_site_url=new_site_url)


@view_config(name="delete-site", context=ctx.Site, request_method='GET')
def delete_site(context, request):
    """Delete an existing site.
    """
    context.delete()
    # Respond
    return HTTPFound(location=request.resource_url(context.__parent__))
