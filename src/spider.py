import requests
from bs4 import BeautifulSoup
from celery import Celery
from decouple import config
from src.db.pages import Pages
from src.db import DB
from src.db.links import Links
from time import sleep


app = Celery('spider', broker=config('CELERY_BROKER'))


@app.task
def spider(id_url):

  page_id = id_url[0]
  url = id_url[1]
  all_links = []

  res = requests.get(url)
  soup = BeautifulSoup(res.text, 'html.parser')

  for link in soup.find_all('a', href=True):

    if link['href'].startswith('http'):
      all_links.append(link['href'])
  # check if page id is in links, delete all data with page id
  # set is_scraping in pages table where id == page_id to True
  # scrap
  # insert into DB
  sleep(3)
  for link in all_links[:10]:
    Links(DB().connect()).insert(page_id, link)
  # set is_scraping in pages table where id == page_id to False


print(spider(Pages(DB.connect()).get_url(1)))
