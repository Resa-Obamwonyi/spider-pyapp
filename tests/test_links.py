import unittest
from src.db import DB
from src.db.links import Links


class TestDB(unittest.TestCase):

  def setUp(self) -> None:
    self.exec = Links(DB.connect())

  def test_insert(self):
    ''' Test insert into links table '''
    DB.setup()
    DB.seed()
    value = self.exec.insert(1, 'https://www.google.com/')
    self.assertEqual(value, None)

  def test_select(self):
    ''' Test select from links table '''
    DB.setup()
    value = self.exec.select()
    self.assertIsNotNone(value)

  def test_select_by_id(self):
    ''' Test selection of specific data from links table by id '''
    DB.setup()
    DB.seed()
    self.exec.insert(1, 'https://www.google.com/')
    value = self.exec.select_by_id(1)
    self.assertIsNotNone(value)
    self.assertEqual(type(value), tuple)

  def test_select_by_page_id(self):
    ''' Test selection of specific data from links table by page_id '''
    DB.setup()
    value = self.exec.select_by_page_id(1)
    self.assertIsNotNone(value)
    self.assertEqual(type(value), list)

  def test_delete_by_id(self):
    ''' Test deletion of specific data in links table by id'''
    DB.setup()
    value = self.exec.delete_by_id(1)
    self.assertEqual(value, None)


  def test_delete_by_page_id(self):
    ''' Test deletion of specific data in links table by page_id'''
    DB.setup()
    DB.seed()
    value = self.exec.delete_by_page_id(1)
    self.assertEqual(value, None)


  def tearDown(self) -> None:
    self.exec = None








