# 查询数据

# 查询表中所有数据

# 导入之前做好的ORM表和引擎
from my_create_table import User, engine
# 写入数据库，首先打开数据库会话，直白就是创建一个操作数据库的窗口
from sqlalchemy.orm import sessionmaker

# 创建sessionmaker会话对象，将数据库引擎engine交给sessionmaker
Session = sessionmaker(engine)
# 打开会话对象Session
db_session = Session()

# 1. select * from user 查询user表中的所有数据
# 语法是这样的 使用 db_session 会话 执行User表 query(User) 取出全部数据 all()
user_all_list = db_session.query(User).all()
print(user_all_list)  # [<my_create_table.User object at 0x0000022C81769B00>,...]
print(user_all_list.__dir__())

for item in user_all_list:
	print(item.id,item.name)  # ORM对象 直接使用调用属性的方法 拿出对应字段的值

db_session.close()

# 条件查询:
# 查询id>=2的数据
user = db_session.query(User).filter(User.id >= 2)
print(user)  # SELECT user.id AS user_id, user.name AS user_name  # 显示原生sql
for item in user:
	print(item.id, item.name)


