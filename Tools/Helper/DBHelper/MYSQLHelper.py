from flask import Flask
import pymysql
import time
from DBUtils.PooledDB import PooledDB, SharedDBConnection


class MYSQLHelper(object):
    def __init__(self, host, port, dbuser, password, database):
        self.pool = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
            maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制，连接使用次数过多会有缓存，有时需要使用最新的
            setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
            maxshared=3,
            # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            ping=0,
            # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
            host=host,
            port=int(port),
            user= dbuser,
            password=password,
            database= database,
            charset='utf8',
        )


    def get_conn(self):
        """
        连接数据库
        :return: conn, cursor
        """
        conn = self.pool.connection()  # 数据库连接
        cursor = conn.cursor(pymysql.cursors.DictCursor)  # 数据库指针
        return conn, cursor


    def reset_conn(self,conn, cursor):
        """
         :param conn: 数据库连接
         :param cursor: 数据库指针
         :return: Null
         """
        cursor.close()
        conn.close()


    def fetch_all(self,sql, args):
        """
        :param sql: sql语句
        :param args: sql语句的参数
        :return: 查询结果
        """
        conn, cursor = self.get_conn()
        cursor.execute(sql, args)
        result = cursor.fetchall()
        self.reset_conn(conn, cursor)
        return result

    def insert_one(self,sql,args):
        conn,cursor=self.get_conn()
        res=cursor.execute(sql,args)
        conn.commit()
        self.reset_conn(conn, cursor)
        return res

    def update(self,sql,args):
        conn,cursor=self.get_conn()
        result = cursor.execute(sql,args)
        conn.commit()
        self.reset_conn(conn, cursor)
        return result