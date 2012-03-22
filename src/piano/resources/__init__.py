"""Application resources, documents, and models.

:mod:`piano.resources`
----------------------

.. autofunction:: create_root

"""
from piano.resources import contexts as ctx
from pyramid.config import Configurator
from pyramid.response import Response

def create_root(request):
    """Create the context tree and wires parent/child classes together.
    """
    app = ctx.App
    root = ctx.Root(request)
    root.app = app
    #Return root
    return root