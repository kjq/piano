"""
:mod:`sample.home.models`
-------------------------

"""
from piano.resources.documents import PageData

class PageModel(PageData):
    structure = {
        'intro_message':unicode,
        'intro_image':str
    }
    default_values = {
        'intro_message':'hello world!',
        'intro_image':'some_image.jpg'
    }