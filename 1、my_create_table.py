# 创建数据表:
# my_create_table.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()  # 实例化官宣模型  Base就是ORM模型


class User(Base):  # 继承Base , Model
	__tablename__ = 'user'  # 创建表名为user

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(32), index=True)  # string 相当于sql里的char


# 在数据库中创建数据表 或  连接数据库
from sqlalchemy import create_engine

# 创建数据库引擎
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/ceshi1?charset=utf8")

# 自动检索所有继承Base的ORM对象，并且创建所有数据表
Base.metadata.create_all(engine)
