# 修改数据

# 导入之前做好的ORM表和引擎
from my_create_table import User, engine
# 写入数据库，首先打开数据库会话，直白就是创建一个操作数据库的窗口
from sqlalchemy.orm import sessionmaker

# 创建sessionmaker会话对象，将数据库引擎engine交给sessionmaker
Session = sessionmaker(engine)
# 打开会话对象Session
db_session = Session()

# 更新某条数据
# UPDATE user SET name="NBDragon" WHERE id=2 更新一条数据
# 将id=2的用户名更改为古天乐
res = db_session.query(User).filter(User.id == 2).update({"name": "古天乐"})
print(res)  # 1    res就是我们当前这句更新语句所更新的行数
db_session.commit()
db_session.close()

# 更新多条数据
# 将id小于等于4的name改为xjk
res = db_session.query(User).filter(User.id <=4).update({"name":"sirxy"})
print(res)
db_session.commit()
db_session.close()

