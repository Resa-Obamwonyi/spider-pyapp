from celery import Celery
from decouple import config
from src.spider import spider
from src.db.pages import Pages
from src.db import DB


# Celery Task
app = Celery('main', broker=config('CELERY_BROKER'), backend=config('CELERY_BACKEND'))

@app.task
def test():
  return spider(1)



# some tests with pages()
DB.pages().get_url(2)
DB.pages().find_by_id(1)
DB.pages().update_by_id()


# some tests with links
DB.links().select()
DB.links().insert(3,'https://google.com')
DB.links().delete_by_page_id(2)


