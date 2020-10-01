import unittest
from src.spider import spider


class SpiderTest(unittest.TestCase):

    def test_correct_page_id(self):
      ''' tests correct page id '''
      self.assertEqual(spider(1), None)

    def test_wrong_page_id(self):
      ''' tests wrong page_id '''
      with self.assertRaises(ValueError):
        self.assertEqual(spider('2'), None)

    def test_zero_page_id(self):
      ''' tests zero input page_id '''
      with self.assertRaises(ValueError):
        value = spider(0)
        self.assertEqual(spider(0), value)

