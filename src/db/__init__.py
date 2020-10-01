import psycopg2
from decouple import config
from src.db import pages
from src.db import links


class DB:

  @classmethod
  def server_conn(cls):
    ''' connects to server and creates database, returns server connection object '''

    connect = psycopg2.connect(
      user=config('DB_USER'),
      password=config('DB_PASSWORD'),
      host=config('DB_HOST'),
      database=None
    )
    cursor = connect.cursor()
    connect.autocommit = True

    # create the database
    cursor.execute('DROP DATABASE IF EXISTS serenedb;')
    cursor.execute('CREATE DATABASE serenedb;')
    return connect

  @classmethod
  def connect(cls):
    ''' Connect to the database and returns the connection object '''

    try:
      connection = psycopg2.connect(
        user=config('DB_USER'),
        password=config('DB_PASSWORD'),
        host=config('DB_HOST'),
        database=config('DB_NAME')
      )
      connection.autocommit = True
      return connection

    except psycopg2.Error as error:
      return error

  @classmethod
  def setup(cls):
    ''' Executes the structure SQL script '''

    cursor = cls.connect().cursor()
    try:
      with open('src/schemas/structure.sql') as file:
        sql = file.readlines()
        for line in sql:
          cursor.execute(line)

    except psycopg2.Error as error:
      print(error)

  @classmethod
  def seed(cls):
    ''' Execute the seed SQL script '''
    cursor = cls.connect().cursor()
    cls.setup()
    try:
      with open('src/schemas/seed.sql') as file:
        sql = file.readlines()
        for line in sql:
          cursor.execute(line)
    except psycopg2.Error as error:
      return error

  @classmethod
  def links(cls):
    ''' Returns a reference to the links interface'''
    return links.Links(cls.connect())

  @classmethod
  def pages(cls):
    ''' Returns a reference to the pages interface'''
    cls.seed()
    return pages.Pages(cls.connect())

