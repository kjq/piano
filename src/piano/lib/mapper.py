"""
:mod:`piano.lib.mapper`
-------------------------------

.. autoclass:: Mapper
   :members:
         
"""

class Mapper():
    """Maps one object or dictionary to another based on a set of field
    mappings.
    
    """
    _source = None
    _target = None
    _mappings = None
    
    def __init__(self):
        self._mappings = []
        
    def source(self, source):
        """Provider of the data in the mappings.
        """
        self._source = source
        return self
    
    def target(self, target):
        """Consumer of the data in the mappings.
        """
        self._target = target
        return self
    
    def field(self, infield, outfield=None):
        """Maps the infield to the outfield.  If the outfield is left blank
        it is assumed both are the same name.
        """
        if outfield is None:
            outfield = infield
        self._mappings.append( (infield, outfield) )
        return self
    
    def build(self):
        """Process the mappings and returns the updated target with the
        mapped values.
        """
        for sk,tk in self._mappings:
            sattrib = None
            #Get source value
            try:
                sattrib = getattr(self._source, sk)
            except:
                sattrib = self._source[sk]
            #Set target value if it has been found in the source first
            try:
                setattr(self._target, tk, sattrib)
            except:
                self._target[tk] = sattrib
        return self._target