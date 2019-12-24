import unittest
import io
import json

from nlptools.utils import Dict

class TestDict(unittest.TestCase):
    def setUp(self):
        self.d = Dict()
        self.d.test = 'hello world'
        self.d.test2 = 'foo'

    def test_dict(self):
        self.assertEqual(self.d.test, 'hello world')
        self.assertEqual(self.d.test2, 'foo')

    def test_keys(self):
        self.assertIn('test', self.d.keys())
        self.assertIn('test2', self.d.keys())

    def test_todict(self):
        self.assertIsInstance(self.d.todict(), dict)
        self.assertIn('test', self.d.todict())
        self.assertIn('test2', self.d.todict())

    def test_deep(self):
        d = Dict()
        d.hello.world = 'test'
        dd = d.todict()
        self.assertEqual(dd['hello']['world'], 'test')

        d.foo = {
            'test': 'foo'
        }
        dd = d.todict()
        self.assertEqual(dd['foo']['test'], 'foo')

if __name__ == "__main__":
    unittest.main()
