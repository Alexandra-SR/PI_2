from database import connector
from model import entities

db = connector.Manager()
engine = db.createEngine()

session = db.getSession(engine)

dbResponse = session.query(entities.Docs)
data = dbResponse[:]


for doc in data:
    print(doc.id, doc.sent_from_username, doc.sent_to_username, doc.location)


# dbResponse = session.query(entities.User)
# data = dbResponse[:]


# for user in data:
#     print(user.username, user.name, user.lastname)
