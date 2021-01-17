from pymysql import connect

class Nebula(object):
    def __init__(self):
        self.conn = connect(
            host = '1.203.144.58',
            port = 3306,
            user = 'debian-sys-maint',
            password = 'NbiTAGtSBbVbjyNI',
            databases = 'nebula',
            charset = 'utf8'
        )
        self.cursor = self.conn.cursor()
    
    def __del__(self):
        self.cursor.close()
        self.conn.close()