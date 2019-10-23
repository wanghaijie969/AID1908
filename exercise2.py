"""
练习 ： 使用数据库支持登录注册
    注册：输入信息--存储到数据库
    user : id  name  passwd
    要求 ：用户名不能重复
    登录： 输入信息--通过数据库查询比对
"""

import pymysql

class Database:
    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='123456',
                             database='stu',
                             charset='utf8')

        # 生成游标对象 (操作数据库，执行sql语句)
        self.cur = self.db.cursor()

    def close(self):
        # 关闭游标和数据库连接
        self.cur.close()
        self.db.close()

    def register(self,name,passwd):
        # 判断用户名是否重复
        sql="select name from user where name=%s;"
        self.cur.execute(sql,[name])
        result = self.cur.fetchone()
        if result:
            print("该用户存在")
            return
        try:
            sql="insert into user (name,passwd) \
            values (%s,%s);"
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
        except:
            self.db.rollback()

if __name__ == '__main__':
    db = Database()
    db.register('zhang','123')
    db.close()
