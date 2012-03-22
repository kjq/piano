"""
:mod:`sample.contactus.models`
------------------------------

"""
from piano.resources import documents as d

class PageModel(d.PageData):
    structure = {
        'some_message':unicode,
        'some_image':str
    }
    default_values = {
        'some_message':'goodbye world!',
        'some_image':'another_image.jpg'
    }