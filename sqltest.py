#! /usr/bin/env python
#coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()



from sqlalchemy import Column, Integer, String
from yourapplication.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
	name_interest = Column(String(50))
	id_interest = (Integer)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
		self.name_interest = name_interest
		self.id_interest = id_interest

    def __repr__(self):
        return '<User %r>' % (self.name)



def init_db():
    # 在这里导入定义模型所需要的所有模块，这样它们就会正确的注册在
    # 元数据上。否则你就必须在调用 init_db() 之前导入它们。
    import yourapplication.models
    Base.metadata.create_all(bind=engine)


from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String

class User(Base):
	__tablename__ = 'users'
	
	id = Column(Integer, primary_key=True)
	name = Column(String)
	fullname = Column(String)
	password = Column(String)

	def __init__(self, name, fullname, password):
		self.name = name
		self.fullname = fullname
		self.password = password
		
	def __repr__(self):
		return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)
	
User.__table__
User.__mapper__
Base.metadata.create_all(engine)
ed_user = User('ed', 'Ed Jones', 'edspassword')

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)  # once engine is available
session = Session()

session.add(ed_user)
session.commit()

our_user = session.query(User).filter_by(name='ed').first() 

session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all()

for instance in session.query(User).order_by(User.id): 
	print instance.name, instance.fullname

for name, fullname in session.query(User.name, User.fullname): 
	print name, fullname
	
for row in session.query(User, User.name).all(): 
	print row.User, row.name
	
for row in session.query(User.name.label('name_label')).all(): 
	print(row.name_label)






if __name__ == "__main__":
    init_db()

