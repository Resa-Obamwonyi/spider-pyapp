# Show examples of how you would use ALL your implementations here

from src.db import DB

db = DB.pages()

# print(db.update_by_id(1)) # updates to true
# print(db.update_by_id(1)) # updates back to false

print(db.get_url(2))