"""
:mod:`sample.home.views`
------------------------

.. autofunction:: say_hello

.. autofunction:: get_some_data

"""
def say_hello(context, msg):
    """Sets a value in the context for use on a page.
    """
    context.write('This page ID is ' + str(context['page_id']))
    return ''

def get_some_data(context):
    """Returns a dict with data to the page.
    """
    return { 
        'key1' : 'Hello World!',
        'key2' : 'Goodbye World!',
        'key3' : 'Foobar...'}