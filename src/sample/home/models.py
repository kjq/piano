"""
:mod:`sample.home.models`
-------------------------

"""
from piano.resources import documents as d

class PageModel(d.PageData):
    structure = {
        'intro_message':unicode,
        'intro_image':str
    }
    default_values = {
        'intro_message':'hello world!',
        'intro_image':'some_image.jpg'
    }