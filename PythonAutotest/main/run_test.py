#encoding=utf-8	
import sys
#指定运行路径
sys.path.append('E:/pythonworkspace/PythonAutotest')
from base.run_method import RunMethod
from data.get_data import GetData
from util.common import CommonUtil
class RunTest():
	def __init__(self):
		self.run_method = RunMethod()
		self.data = GetData()
		self.com_util = CommonUtil()
	# 程序执行
	def go_on_run(self):
		res = None
		#获取case个数（获取有数据的单元格行）
		rows_count = self.data.get_case_lines()
		#循环判断要执行的case,跳过第一行标题开始循环
		for i in range(1,rows_count):
			# print i
			#获取url
			url = self.data.get_request_url(i)
			# print url
			#获取请求类型
			method = self.data.get_request_method(i)
			# print method
			#获取是否执行
			is_run = self.data.get_is_run(i)
			# print is_run
			#获取数据
			data = self.data.get_data_for_json(i)
			# print data
			expect = self.data.get_expect_data(i)
			#获取header(默认demo)
			header = self.data.demo_header()
			#获取excel中指定header
			# header = self.data.is_header(i)
			# print header
			# #判断is_run的值为true时执行
			if is_run:
				res = self.run_method.run_main(method,url,data,header)
				# print res
				#判断返回结果与预期结果比对
				if self.com_util.is_contain(expect,res):
					print "pass"
				else:
					print "false"


				
if __name__ == '__main__':
	run = RunTest()
	run.go_on_run()