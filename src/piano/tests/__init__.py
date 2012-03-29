import unittest

from pyramid import testing
from piano.lib.mapper import Mapper as m
        
class DummySource():
    def __init__(self):
        self.key1 = 'abc'
        self.key2 = 'xyz'
        self.key3 = 'qrs'

class MapperTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        #Setup test instances
        self.dummy_class = DummySource()
        self.dummy_dict = dict(
            dkey1='123',
            dkey2=456,
            key3='yui')

    def tearDown(self):
        testing.tearDown()

    def test_simple(self):
        self.assertEqual(True, True)

    def test_dict_to_clz_mapping(self):
        dict_to_clz = m(self.dummy_dict, self.dummy_class)
        #Process
        result = dict_to_clz \
                    .field('dkey1', 'key1') \
                    .field('dkey2', 'key2') \
                    .field('key3') \
                    .build()
        #Validate
        self.assertIsInstance(result, DummySource)
        self.assertEqual('123', self.dummy_class.key1)
        self.assertEqual(456, self.dummy_class.key2)
        self.assertEqual('yui', self.dummy_class.key3)

    def test_clz_to_dict_mapping(self):
        clz_to_dict = m(self.dummy_class, self.dummy_dict)
        #Process
        result = clz_to_dict \
                    .field('key1', 'dkey1') \
                    .field('key2', 'dkey2') \
                    .field('key3') \
                    .build()
        #Validate
        self.assertEqual('abc', self.dummy_dict['dkey1'])
        self.assertEqual('xyz', self.dummy_dict['dkey2'])
        self.assertEqual('qrs', self.dummy_dict['key3'])
        
