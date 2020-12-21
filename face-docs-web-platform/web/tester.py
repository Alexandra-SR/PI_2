from database import connector
from model import entities

db = connector.Manager()
engine = db.createEngine()

session = db.getSession(engine)

# dbResponse = session.query(entities.Docs)
# data = dbResponse[:]


# for doc in data:
#     print(doc.id, doc.sent_from_username, doc.sent_to_username, doc.location, doc.fileName)
# engine.execute(f"""DELETE FROM users""")

# user_from = 'joaquin.ramirez'
# query = f"""select * from docs"""
# res = session.execute(query)
# d, a = {}, []

# for rowproxy in res:
#     for column, value in rowproxy.items():
#         d = {**d, **{column: value}}
#     a.append(d)
# print(a)
dbResponse = session.query(entities.User)
data = dbResponse[:]
for user in data:
    print(user.username, user.name, user.lastname)