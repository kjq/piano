"""
:mod:`piano.views.pages`
------------------------

.. autofunction:: piano.views.pages.view_page

.. autofunction:: piano.views.pages.create_page

"""
from piano.lib import constants as c
from piano.lib import helpers as h
from piano.lib import mvc
from piano.resources import contexts as ctx
from pyramid.httpexceptions import HTTPFound
from pyramid.renderers import render_to_response
from pyramid.view import view_config

template_name = lambda s,t: ':'.join([s, t])

@view_config(context=ctx.Page, request_method='GET')
def view_page(context, request):
    """Renders a page using its associated template in either VIEW mode.
    """
    template = template_name(context.source, c.VIEW_TEMPLATE)
    edit_page_url = request.resource_url(context, 'edit-page')
    save_page_url = request.resource_url(context, 'save-page')
    # Respond
    return render_to_response(
        template,
        mvc.PageModel(
            context,
            edit_page_url=edit_page_url,
            save_page_url=save_page_url),
        request=request)

@view_config(name='edit-page', context=ctx.Page, request_method='GET')
@view_config(name='edit-page', context=ctx.Page, request_method='POST')
def edit_page(context, request):
    """Renders a page using its associated template in either EDIT mode.
    """
    template = template_name(context.source, c.EDIT_TEMPLATE)
    save_page_url = request.resource_url(context, 'edit-page')
    # Handle submission
    if 'form.submitted' in request.params:
        title = request.params['page.title']
        slug = str(h.urlify(request.params['page.slug']))
        # Parse the data elements
        data = dict((k.replace(c.DATA_PREFIX, ''), v)
                    for k, v in request.POST.items() if k.startswith(c.DATA_PREFIX))
        # Persist Page
        page = ctx.Page(
            id=context.id,
            key=slug,
            parent=context,
            title=title,
            slug=slug,
            data=data).update()
        return HTTPFound(location=request.resource_url(context, page.__name__))
    # Respond
    return render_to_response(
        template,
        mvc.PageModel(
            context,
            edit_page_url=None,
            save_page_url=save_page_url),
        request=request)

@view_config(name='add-page', context=ctx.Site, renderer='piano.web.templates.page:add.mako', request_method='GET')
@view_config(name='add-page', context=ctx.Site, request_method='POST')
@view_config(name='save-page', context=ctx.Page, request_method='POST')
def create_page(context, request):
    """Add or save a page.
    """
    # Handle submission
    if 'form.submitted' in request.params:
        title = request.params['title']
        slug = str(h.urlify(title))
        source = request.params['source']
        # Persist Page (home)
        page = ctx.Page(
            key=slug,
            parent=context,
            title=title,
            slug=slug,
            source=source).create()
        return HTTPFound(location=request.resource_url(context, page.__name__))
    save_page_url = request.resource_url(context, 'save-page')
    # Respond
    return dict(page_title="Edit Page",
                page_slug=context.__name__,
                save_page_url=save_page_url)