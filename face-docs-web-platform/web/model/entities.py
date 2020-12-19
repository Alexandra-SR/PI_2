from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class User(connector.Manager.Base):
    __tablename__ = 'users'
    username = Column(String(20), Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    lastname = Column(String(50))
    #password = Column(String(12))

class Docs(connector.Manager.Base):
    __tablename__ = 'docs'
    id = Column(Integer, Sequence('docs_id_seq'), primary_key=True)
    sent_from_username = Column(Integer, ForeignKey('users.username'))
    sent_to_username = Column(Integer, ForeignKey('users.username'))
    location = Column(String(50))
    fileName = Column(String(50))
    sent_from = relationship(User, foreign_keys=[sent_from_username])
    sent_to = relationship(User, foreign_keys=[sent_to_username])
