class Pages:
  def __init__(self, connect):
    self.cursor = connect.cursor()

  def select(self):
    self.cursor.execute('SELECT * FROM pages')
    return self.cursor.fetchall()

  def select_urls(self):
    self.cursor.execute('SELECT url FROM pages')
    return self.cursor.fetchall()

  def find_by_id(self, id):
    self.cursor.execute('SELECT * FROM pages WHERE id = %s', (id,))
    return self.cursor.fetchone()

  def get_url(self, id):
    self.cursor.execute('SELECT id, url FROM pages WHERE id = %s', (id,))
    url = self.cursor.fetchone()
    return url

  def update_by_id(self, id):
    self.cursor.execute('SELECT is_scraping FROM pages WHERE id = %s', (id,))
    value = self.cursor.fetchone()
    is_scraping = value[0]

    if is_scraping == True:
      self.cursor.execute('UPDATE pages SET is_scraping = %s WHERE id = %s', (False, id))

    if is_scraping == False:
      self.cursor.execute('UPDATE pages SET is_scraping = %s WHERE id = %s', (True, id))

  def delete_by_id(self, id):
    self.cursor.execute('DELETE FROM pages WHERE id = %s', (id,))

