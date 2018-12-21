#coding:utf-8
from util.operation_excel import OperationExcel
import dataconfig
from util.operation_json import OperationJson
class GetData:
	def __init__(self):
		self.opera_excel = OperationExcel()
		global host
		host = 'http://192.168.1.11:8050'
	#获取excel行数，case个数
	def get_case_lines(self):
		return self.opera_excel.get_lines()

	#获取是否执行
	def get_is_run(self,row):
		flag = None
		col = int(dataconfig.get_run())
		run_model = self.opera_excel.get_cell_value(row,col)
		if run_model == 'yes':
			flag = True
		else:
			flag = False
		return flag

	#是否携带header
	def is_header(self,row):
		col = int(dataconfig.get_header())
		header = self.opera_excel.get_cell_value(row,col)
		if header == 'login':
			header = dataconfig.get_header_value()
			return header
		elif header == 'load':
			header = dataconfig.get_header_value_load()
			return header
		else:
			return None

	#获取请求方式
	def get_request_method(self,row):
		col = int(dataconfig.get_run())
		request_method = self.opera_excel.get_cell_value(row,col)
		return request_method

	#获取url
	def get_request_url(self,row):
		col = int(dataconfig.get_url())
		url = self.opera_excel.get_cell_value(row,col)
		return host+url

	#获取请求数据
	def get_request_data(self,row):
		col = int(dataconfig.get_data())
		data = self.opera_excel.get_cell_value(row,col).encode('utf-8')
		if data == '':
			return None
		else:
			return data

	#通过获取关键字拿到data数据
	def get_data_for_json(self,row):
		opera_json = OperationJson()
		request_data = opera_json.get_data(self.get_request_data(row))
		return request_data

	#获取预期结果
	def get_expect_data(self,row):
		col = int(dataconfig.get_expect())
		expect = self.opera_excel.get_cell_value(row,col)
		if expect == '':
			return None
		return expect


#通过sql获取预期结果
	# def get_expcet_data_for_mysql(self,row):
	# 	op_mysql = OperationMysql()
	# 	sql = self.get_expcet_data(row)
	# 	res = op_mysql.search_one(sql)
	# 	return res.decode('unicode-escape')
	#
	# def write_result(self,row,value):
	# 	col = int(data_config.get_result())
	# 	self.opera_excel.write_value(row,col,value)

	#获取依赖数据的key
	def get_depend_key(self,row):
		col = int(dataconfig.get_data_depend())
		depent_key = self.opera_excel.get_cell_value(row,col)
		if depent_key == "":
			return None
		else:
			return depent_key

	#判断是否有case依赖
	def is_depend(self,row):
		col = int(dataconfig.get_case_depend())
		depend_case_id = self.opera_excel.get_cell_value(row,col)
		if depend_case_id == "":
			return None
		else:
			return depend_case_id

	#获取数据依赖字段
	def get_depend_field(self,row):
		col = int(dataconfig.get_field_depend())
		data = self.opera_excel.get_cell_value(row,col)
		if data == "":
			return None
		else:
			return data

	#写入结果
	def write_result(self,row,value):
		col = int(dataconfig.get_result())
		self.opera_excel.write_value(row, col, value)

if __name__ == '__main__':
	op = GetData()
	print op.get_request_url(1)