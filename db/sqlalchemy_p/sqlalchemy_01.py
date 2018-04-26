# -*- coding: utf-8 -*-
# description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/26'

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    # 结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:root@localhost:3306/db', echo=True)
# Base.metadata.create_all(engine)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id='003', name='bill')
session.add(new_user)
session.commit()
session.close()

#查询
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='001').one()
print(user)

