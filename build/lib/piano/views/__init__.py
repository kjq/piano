"""General Views

:mod:`piano.views`
---------------------

.. autofunction:: index

"""
from collections import namedtuple
from piano.resources import contexts as ctx
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

@view_config(context=ctx.Root)
def index(context, request):
    """Root view of the system.
    
    This is a temporary hack into the specific application.
    """
    return HTTPFound(location=request.resource_url(context, 'sample'))