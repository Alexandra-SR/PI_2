from database import connector
from model import entities

db = connector.Manager()
engine = db.createEngine()

session = db.getSession(engine)

dbResponse = session.query(entities.Docs)
data = dbResponse[:]


# for doc in data:
#     print(doc.id, doc.sent_from_username, doc.sent_to_username, doc.location, doc.fileName)
# engine.execute(f"""INSERT INTO docs VALUES (3, 'edir.vidal', 'joaquin.ramirez', 'static/uploads/edir.vidal_joaquin.ramirez_logo.png', 'logo.png')""")

user_from = 'joaquin.ramirez'
query = f"""SELECT * FROM users u INNER JOIN (SELECT sent_to_username, location, fileName  FROM docs WHERE sent_from_username = 'edir.vidal') 
                f ON u.username = f.sent_to_username;"""
res = session.execute(query)
d, a = {}, []

for rowproxy in res:
    for column, value in rowproxy.items():
        d = {**d, **{column: value}}
    a.append(d)
print(a)
# # dbResponse = session.query(entities.User)
# # data = dbResponse[:]


# # for user in data:
# #     print(user.username, user.name, user.lastname)
