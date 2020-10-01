
class Links:
  def __init__(self, connect):
    self.cursor = connect.cursor()

  def insert(self, page_id, url):
    self.cursor.execute('INSERT INTO links (page_id, url) VALUES (%s , %s )', (page_id, url))

  def select(self):
    self.cursor.execute('SELECT * FROM links')
    return self.cursor.fetchall()

  def select_by_id(self, id):
    self.cursor.execute('SELECT * FROM links WHERE id = %s', (id,))
    return self.cursor.fetchone()

  def select_by_page_id(self, page_id):
    self.cursor.execute('SELECT * FROM links WHERE page_id = %s', (page_id,))
    return self.cursor.fetchall()

  def delete_by_id(self, id):
    self.cursor.execute('DELETE FROM links WHERE id = %s', (id,))

  def delete_by_page_id(self, page_id):
    self.cursor.execute('DELETE FROM links WHERE page_id = %s', (page_id,))


