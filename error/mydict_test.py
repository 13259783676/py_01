#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/24'

import unittest
from mydict import Dict


class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
        print('end')

if __name__ == '__main__':
    unittest.main()