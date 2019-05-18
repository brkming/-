import pymysql


# 用来操作数据库的类
class MySQLCommand(object):
    # 类的初始化
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306  # 端口号
        self.user = 'root'  # 用户名
        self.password = "123456"  # 密码
        self.db = "testdb"  # 库
        self.table = "infotimal"  # 表

    def connectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                        passwd=self.password, db=self.db, charset='utf8')
            self.cursor = self.conn.cursor()
        except:
            print('connect mysql error.')

    # 查询数据
    def queryMysql(self):
        global row
        sql = "SELECT * FROM " + self.table
        self.cursor.execute(sql)
        row = list(self.cursor.fetchall())

        return row
class test():
    mySQLCommand = MySQLCommand()
    mySQLCommand.connectMysql()
    mySQLCommand.queryMysql()

