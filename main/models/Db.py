from Config import Config

import sys
import os
dir = os.path.dirname(__file__)
sys.path.insert(0, dir + '/../')


Config.load()
host = Config.get('db', 'host')
user = Config.get('db', 'user')
password = Config.get('db', 'password')
database = Config.get('db', 'database')
dbms = Config.get('db', 'dbms')


class Db:
    def __init__(self):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.dbms = dbms.lower()

        if self.dbms.lower() == 'mysql':
            import MySQLdb
            self.conn = MySQLdb.connect(
                self.host,
                self.user,
                self.password,
                self.sqldb
            )
        elif self.dbms.lower() == 'postgresql':
            import psycopg2
            self.conn = psycopg2.connect("""
            dbname='{}' user='{}' host='{}' password='{}'
            """.format(self.database, self.user, self.host, self.password))

        cursor = self.conn.cursor()

        def query(self, sql, params=None):
            if params is not None:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
        return cursor

    def commit(self):
        self.conn.commit()

    def truncate(self, table):
        sql = """TRUNCATE TABLE %s""" % (table)
        self.query(sql)
        self.conn.commit()

    def close(self):
        self.conn.close()
