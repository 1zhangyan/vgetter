import pymysql

class Dbget:
    def __init__(self):
        self.db = pymysql.connect(host="182.92.236.73", user="root", passwd="2001210541", database="zhangyan",autocommit=True)
        self.gift_map = {}
        
    def insertInto(self ,type, name):
        if (self.gift_map.get(type, -1) == -1):
            self.gift_map[type] = name
            sql = "INSERT INTO huya_gift_info (gift_type,name) VALUES ("+ str(type) + ",'" + name + "');"
            try:
                self.db.cursor().execute(sql)
            except pymysql.OperationalError:
                try :
                    self.db = pymysql.connect(host="182.92.236.73", user="root", passwd="2001210541", database="zhangyan",autocommit=True)
                    self.db.cursor().execute(sql)
                except Exception as e :
                    print(e)
            except Exception as e:
                print(e)
    
    def close(self):
        self.db.close()


    