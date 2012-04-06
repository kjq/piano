"""MongoDB setup and utilities.

:mod:`piano.lib.mongo`
-----------------------

.. autofunction:: setup_db

.. autofunction:: ensure_indexes

.. autofunction:: mongodb_subscriber

.. autofunction:: mongodb_cleanup_subscriber

"""
from piano import constants as c
from mongokit import Connection
from pymongo import ASCENDING as ASC
from pyramid.events import NewRequest
from pyramid.events import subscriber
import logging

logger = logging.getLogger(__name__)

try:
    conn = Connection()
except:
    #Create a dummy connection and db
    conn = {}


def setup_db(config, settings, full_index=False):
    """Sets up MongoDB, registers the connection (and its cleanup) in the
    request, and ensures all of the indexes are set.
    """
    try:
        #Place connection (mongokit) into the registry
        config.registry.settings[c.MONGO_CONN] = conn
        #Setup indexes
        ensure_indexes(full_index)
    except Exception, x:
        logger.error(x.message)
    else:
        logger.debug('Registered Mongo Connection')


def ensure_indexes(full_index=False):
    """Hard-coded utility function to ensure the proper indexes are set across
    all of the databases and collections (excluding system ones).
    """
    logger.info('Ensuring indexes on')
    try:
        db_names = filter(lambda x: not x.startswith('local'), conn.database_names())
        for db_name in db_names:
            db = conn[db_name]
            #Sites
            logger.info('  %s database', db_name)
            sites = db['sites']
            logger.info('    sites')
            sites.ensure_index('slug', unique=True)
            if full_index:
                sites.reindex()
            #Pages
            pages_list = filter(lambda x: x.endswith('pages'), db.collection_names())
            for site_name in pages_list:
                logger.info('    %s', site_name)
                site = db[site_name]
                site.ensure_index([
                    ('parent', ASC),
                    ('slug', ASC)],
                    unique=True)
                if full_index:
                    site.reindex()
            #Historys
            history_list = filter(lambda x: x.endswith('history'), db.collection_names())
            for site_name in history_list:
                logger.info('    %s', site_name)
                site = db[site_name]
                site.ensure_index([
                    ('pageid', ASC),
                    ('version', ASC)],
                    unique=True)
                if full_index:
                    site.reindex()
    except Exception, x:
        logger.error(x)


@subscriber(NewRequest)
def mongodb_subscriber(event):
    """Attaches a MongoDB connection to the current request.
    """
    settings = event.request.registry.settings
    conn = settings[c.MONGO_CONN]
    event.request.conn = conn

@subscriber(NewRequest)
def mongodb_cleanup_subscriber(event):
    """Releases the MongoDB connection which was attached to the request.
    """
    def cleanup_callback(request):
        request.conn.close()
    event.request.add_finished_callback(cleanup_callback)
