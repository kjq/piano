"""WSGI entry-point

:mod:`piano`
---------------------

.. autofunction:: main

"""
from piano import constants as c
from piano.lib import mongo
from piano.resources import create_root
from pyramid_beaker import session_factory_from_settings
from pyramid_beaker import set_cache_regions_from_settings
from pyramid.config import Configurator
from pyramid.events import NewRequest
from pyramid.events import subscriber
from pyramid.renderers import JSONP
import logging

logger = logging.getLogger(__name__)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    set_cache_regions_from_settings(settings)
    config = Configurator(settings=settings, root_factory=create_root)
    # Configure renderers
    config.add_renderer('jsonp', JSONP(param_name='callback'))
    # Configure views
    config.add_static_view(name='static', path='piano:static', cache_max_age=3600)
    # Configure session factory  and caching (beaker)
    session_factory = session_factory_from_settings(settings)
    config.set_session_factory(session_factory)
    config.scan()
    # Configure databases (we use a closure to later abstract Mongo)
    def setup_database():
        mongo.setup_db(
            config, 
            settings, 
            full_index=False)
    setup_database()
    logger.debug('Sites WSGI instance ready')
    # Return instance
    return config.make_wsgi_app()