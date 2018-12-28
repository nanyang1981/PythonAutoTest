#coding=utf-8
import  pymssql
import json
#导入sqlsever驱动（mysql驱动：pymysql）
class OperationDB:
	def __init__(self):
		self.conn = pymssql.connect(
                host = '192.168.1.11',
                port='1433',user='sa',
                password='lanyeesoft_123',
                database='jitnew1201',
                charset = 'utf8'
                )
		self.cur = self.conn.cursor(as_dict=True)

	#查询一条数据
	def search_one(self,sql):
		self.cur.execute(sql)
		result = self.cur.fetchone()
		# return str(result)
		return result


if __name__ == '__main__':
	op_sql = OperationDB()
	print(op_sql.search_one("select * from subaccount where subaccountID = 'sub1'"))