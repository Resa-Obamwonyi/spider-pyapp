import requests
from bs4 import BeautifulSoup
from src.db import DB
from src.db.links import Links


def spider(page_id):

  ''' Takes a page id, selects the url linked to page id and runs the scraper
      Scraper takes url and returns a list of urls scraped,
      a maximum of 10 links are inserted into the database '''

  if type(page_id) != int or page_id == 0:
    raise ValueError('Page Id is not valid')

  get_url = DB.pages().get_url(page_id)

  if get_url is None:
      return ValueError('Page Id not found')

  else:
      url = get_url[0]
      all_links = []

      # set is_scraping to True where id == page_id
      DB.pages().update_by_id(True, page_id)

      res = requests.get(url)
      soup = BeautifulSoup(res.text, 'html.parser')

      for link in soup.find_all('a', href=True):

        if link['href'].startswith('http'):
          all_links.append(link['href'])

      # check if page id is in already in links table, delete all data with page id
      DB.links().delete_by_page_id(page_id)

      for link in all_links[:10]:
        # Insert each link into the links table
        Links(DB().connect()).insert(page_id, link)

      # set is_scraping to False in  where id == page_id
      DB.pages().update_by_id(False, page_id)

