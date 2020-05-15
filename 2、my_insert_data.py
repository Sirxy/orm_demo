# 增加数据

from my_create_table import User  # 导入之前做好的ORM表


user1 = User(name="sirxy")  # 使用User ORM模型创建一条数据

# 写入数据库，首先打开数据库会话，直白就是创建一个操作数据库的窗口
from sqlalchemy.orm import sessionmaker

# 导入之前创建好的create_engine
from my_create_table import engine

# 创建sessionmaker会话对象，将数据库引擎engine交给sessionmaker
Session = sessionmaker(engine)

# 打开会话对象Session
db_session = Session()

# 使用db_session会话提交，将db_session中所有指令一次性提交
# db_session.add(user1)
# db_session.commit()

# 增加多个数据
user_list = [
    User(name = "金城武"),
    User(name = "刘德华"),
    User(name = "梁朝伟"),
]
db_session.add_all(user_list)
db_session.commit()


