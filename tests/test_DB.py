import unittest
from src.db import DB


class TestDB(unittest.TestCase):
  def setUp(self) -> None:
    self.exec = DB().server_conn()

  def test_server_creation(self):
    ''' Test connection to server '''
    self.assertIsNotNone(DB.server_conn())

  def test_db_connect(self):
    ''' Test connection to database '''
    self.assertIsNotNone(DB.connect())

  def test_setup(self):
    ''' Test table setup and creation via reading sql '''
    self.assertEqual(DB.setup(), None)

  def test_seed(self):
    ''' Test table insertion '''
    self.assertEqual(DB.seed(), None)

  def test_pages(self):
    ''' Test pages interface '''
    self.assertIsNotNone(DB.pages(), None)

  def test_links(self):
    ''' Test links interface '''
    self.assertIsNotNone(DB.links(), None)

  def tearDown(self) -> None:
    self.exec = None








