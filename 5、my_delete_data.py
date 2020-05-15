# 删除数据


# 导入之前做好的ORM表和引擎
from my_create_table import User, engine
# 写入数据库，首先打开数据库会话，直白就是创建一个操作数据库的窗口
from sqlalchemy.orm import sessionmaker

# 创建sessionmaker会话对象，将数据库引擎engine交给sessionmaker
Session = sessionmaker(engine)
# 打开会话对象Session
db_session = Session()

# 删除单条数据
res = db_session.query(User).filter(User.id==2).delete()
print(res)  # DELETE FROM `user` WHERE id=2;
db_session.commit()
db_session.close()


# 删除多条数据
# DELETE FROM `user` WHERE id>2;
res = db_session.query(User).filter(User.id>2).delete()
db_session.commit()
db_session.close()

