"""
:mod:`piano.views.pages`
------------------------

.. autofunction:: piano.views.pages.edit_page

.. autofunction:: piano.views.pages.new_page

.. autofunction:: piano.views.pages.view_page

"""
from piano import constants as c
from piano.lib import mvc
from piano.resources import contexts as ctx
from pyramid.httpexceptions import HTTPFound
from pyramid.renderers import render_to_response
from pyramid.view import view_config

template_name = lambda s, t: ':'.join([s, t])

@view_config(context=ctx.Page, request_method='GET')
@view_config(name=c.V, context=ctx.Page, request_method='GET')
def view_page(context, request):
    """Renders a page using its associated template in VIEW mode.
    """
    template = template_name(context.source, c.VIEW_TEMPLATE)
    new_page_url = request.resource_url(context, 'new-page')
    edit_page_url = request.resource_url(context, 'edit-page')
    history_page_url = request.resource_url(context, 'history')
    # Respond
    return render_to_response(
        template,
        mvc.PageModel(
            context,
            new_page_url=new_page_url,
            edit_page_url=edit_page_url,
            history_page_url=history_page_url),
        request=request)

@view_config(name='edit-page', context=ctx.Page, request_method='GET')
@view_config(name='edit-page', context=ctx.Page, request_method='POST')
def edit_page(context, request):
    """Renders a page using its associated template in EDIT mode.
    """
    template = template_name(context.source, c.EDIT_TEMPLATE)
    edit_page_url = request.resource_url(context, 'edit-page')
    # Handle submission
    if 'form.submitted' in request.params:
        data = mvc.merge(request.POST.items())
        context.save(data)
        return HTTPFound(location=request.resource_url(context))
    # Respond
    return render_to_response(
        template,
        mvc.PageModel(
            context,
            new_page_url=None,
            edit_page_url=edit_page_url,
            history_page_url=None),
        request=request)

@view_config(name='new-page', context=ctx.Site, renderer='piano.web.templates.page:new.mako', request_method='GET')
@view_config(name='new-page', context=ctx.Site, request_method='POST')
@view_config(name='new-page', context=ctx.Page, request_method='POST')
def new_page(context, request):
    """Adds a new page.
    """
    # Handle submission
    if 'form.submitted' in request.params:
        data = mvc.merge(request.POST.items())
        page = ctx.Page(parent=context)
        page.create(data)
        return HTTPFound(location=request.resource_url(context, page.__name__))
    new_page_url = request.resource_url(context, 'new-page')
    # Respond
    return dict(page_title="New Page",
                page_slug=context.__name__,
                new_page_url=new_page_url)