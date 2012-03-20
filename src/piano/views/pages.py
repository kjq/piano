"""
:mod:`piano.views.page`
---------------------

.. autofunction:: piano.views.pages.view_page

.. autofunction:: piano.views.pages.save_page

"""
from piano.lib import helpers as h
from piano.lib import mvc
from piano.resources import contexts as ctx
from pyramid.httpexceptions import HTTPFound
from pyramid.renderers import render_to_response
from pyramid.view import view_config

@view_config(context=ctx.Page, request_method='GET')
def view_page(context, request):
    """Renders a page using its associated template.
    """
    save_page_url = request.resource_url(context, 'save-page')
    # Respond
    return render_to_response(
        context.template,
        mvc.PageModel(
            context,
            save_page_url=save_page_url),
        request=request)

@view_config(name='add-page', context=ctx.Site, renderer='piano.web.templates.page:add.mako', request_method='GET')
@view_config(name='add-page', context=ctx.Site, request_method='POST')
@view_config(name='save-page', context=ctx.Page, request_method='POST')
def save_page(context, request):
    """Add, edit, and save a page.
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
            source=source).save()
        return HTTPFound(location=request.resource_url(context, page.__name__))
    save_page_url = request.resource_url(context, 'save-page')
    # Respond
    return dict(page_title="Edit Page",
                page_slug=context.__name__,
                save_page_url=save_page_url)