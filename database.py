from datetime import datetime 
import mongomock

db = mongomock.MongoClient()
emails = db.emails.collection

def init_db():
  global emails

  emails.insert_one({
    'eid': 1,
    'subject': 'A Subject',
    'content': 'email content....'
  })

  emails.insert_one({
    'eid': 2,
    'subject': 'A Subject',
    'content': 'email content....'
  })
