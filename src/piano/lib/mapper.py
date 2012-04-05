"""
:mod:`piano.lib.mapper`
-------------------------------

.. autoclass:: Mapper
   :members:
         
"""
from piano import constants as c

def merge(source):
    # Site data
    site_data = dict((k.replace(c.SITE_PREFIX, ''), v)
                          for k, v in source
                              if k.startswith(c.SITE_PREFIX))
    # Page data
    page_data = dict((k.replace(c.PAGE_PREFIX, ''), v)
                          for k, v in source
                              if k.startswith(c.PAGE_PREFIX))
    # Model data
    page_model = dict((k.replace(c.DATA_PREFIX, ''), v)
                          for k, v in source
                              if k.startswith(c.DATA_PREFIX))
    return dict(
        site=site_data,
        page=page_data,
        data=page_model)

class Mapper():
    """Maps one object or dictionary to another based on a set of field
    mappings.
    
    """
    source = None
    target = None
    mappings = None

    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.mappings = []

    def field(self, infield, outfield=None):
        """Maps the infield to the outfield.  If the outfield is left blank
        it is assumed both are the same name.
        """
        if outfield is None:
            outfield = infield
        self.mappings.append((infield, outfield))
        return self

    def build(self):
        """Process the mappings and returns the updated target with the
        mapped values.
        """
        for sk, tk in self.mappings:
            sattrib = None
            #Get source value
            try:
                sattrib = getattr(self.source, sk)
            except:
                sattrib = self.source[sk]
            #Set target value if it has been found in the source first
            try:
                setattr(self.target, tk, sattrib)
            except:
                self.target[tk] = sattrib
        return self.target