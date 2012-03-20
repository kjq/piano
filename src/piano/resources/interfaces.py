"""
:mod:`piano.resources.interfaces`
--------------------------------

.. autoclass:: IApp

.. autoclass:: ISite
   
"""
from zope.interface import Interface

class IApp(Interface):
    """Marker interface for an application context.
    """
    pass

class ISite(Interface):
    """Marker interface for a site context.
    """
    pass