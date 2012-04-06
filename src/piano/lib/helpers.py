"""
:mod:`piano.lib.helpers`
-------------------------

.. autofunction:: now

"""
from webhelpers.text import urlify
import datetime as dt

def now():
    return dt.datetime.utcnow()


def available_pages(app='sample'):
    """Temporary helper function to return a list of available pages for use
    in a site.
    
    This should eventually read from a data-source
    """
    j = lambda a, s, t: ('.'.join([a, s]), t)
    return [
        j(app, 'home', 'Home'),
        j(app, 'contactus', 'Contact Us'),
        j(app, 'sitemap', 'Site Map'),
    ]