#! /usr/bin/env python
#coding=utf-8
#import hashlib
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from initclient import initclient
 
Base = declarative_base()
 
class User(Base):
    __tablename__ = 'users'
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
	email = Column(String)
	screen_name = Column(String)
#	username = Column(String)
#    password = Column(String)
	
 
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
		self.email. = email
		self.screen_name = screen_name
		
#        self.password = hashlib.sha1(password).hexdigest()
		
 
    def __repr__(self):
        return "User('%s','%s', '%s')" % \
        (self.name, self.screen_name, self.email)
 
 
if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:', echo=True)
    ''' 此時只有建立 SQLAlchemy Engine 實例，還沒在記憶體內建立資料，
        只有第一個 SQL 指令被下達時，才會真正連接到資料庫內執行 '''
 
    ''' 真正建立表格是使用 Base.metadata.create_all(engine) '''
    Base.metadata.create_all(engine)
 
    auser = User("user1","username","userpassword")
    print "Mapper:", auser.__mapper__


#if __name__ == '__main__':
#    engine = create_engine('sqlite:///:memory:', echo=False)
#    Base.metadata.create_all(engine)
#	
#    Session = sessionmaker(bind=engine)
#    session = Session()
#
#    user_1 = User("user1", "username1", "password_1")
#    session.add(user_1)
#    row = session.query(User).filter_by(name='user1').first()
#    if row:
#        print 'Found user1'
#        print row
#    else:
#        print 'Can not find user1'
# 
#    session.rollback() # 資料庫回到新增 user1 之前的狀態
# 
#    row = session.query(User).filter_by(name='user1').first()#只是要注意的是 query() 接受的參數為 Mapped Class (例如先前定義的 User 類別)，而不是表格名稱
#    if row:
#        print 'Found user1 after rollback'
#        print row
#    else:
#        print 'Can not find user1 after rollback'
# 
#    user_2 = User("user2", "username2", "password_2")
#    session.add(user_2)
#    session.commit()
#
#for r in session.query(User):#SELECT * FROM user
#    print type(r)
#    print r.name, r.username, r.password
#