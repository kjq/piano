"""
:mod:`piano.lib.rest`
----------------------

.. autofunction:: invoke

"""
import urllib2
import simplejson as json

def invoke(url):
    """Invokes a RESTful URL and converts the response to a Python dict().
    """
    data = None
    try:
        data = urllib2.urlopen(url).read()
    except urllib2.HTTPError, e:
        print "HTTP error: %d" % e.code
    except urllib2.URLError, e:
        print "Network error: %s" % e.reason.args[1]
    finally:
        if data is not None:
            return json.loads(data)