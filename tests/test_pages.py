import unittest
from src.db import DB
from src.db.pages import Pages


class TestDB(unittest.TestCase):

  def setUp(self) -> None:
    self.exec = Pages(DB.connect())

  def test_select(self):
    ''' Test selection  of entire pages table '''
    DB.setup()
    DB.seed()
    value = self.exec.select()
    self.assertIsNotNone(value)

  def test_select_urls(self):
    ''' Test selection of urls from pages table '''
    DB.setup()
    DB.seed()
    value = self.exec.select_urls()
    self.assertIsNotNone(value)

  def test_find_by_id(self):
    ''' Test selection of specific data from pages table by id '''
    DB.setup()
    DB.seed()
    value = self.exec.find_by_id(1)
    self.assertIsNotNone(value)
    self.assertEqual(type(value), tuple)

  def test_get_url(self):
    ''' Test selection of specific url by id'''
    DB.setup()
    DB.seed()
    value = self.exec.get_url(1)
    self.assertIsNotNone(value)
    self.assertEqual(type(value), tuple)

  def test_update_by_id(self):
    ''' Test update is_scraping value by id '''
    DB.setup()
    DB.seed()
    value = self.exec.update_by_id(1)
    self.assertEqual(value, None)

  def test_delete_by_id(self):
    ''' Test selection from pages table '''
    DB.setup()
    DB.seed()
    value = self.exec.delete_by_id(1)
    self.assertEqual(value, None)


  def tearDown(self) -> None:
    self.exec = None








