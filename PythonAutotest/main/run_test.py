#encoding=utf-8	
import sys
#指定运行路径
sys.path.append('E:/pythonworkspace/PythonAutotest')
from base.run_method import RunMethod
from data.get_data import GetData
from util.common import CommonUtil
import json
from data.dependent_data import DependentData
from util.send_email import SendEmail
class RunTest():
	def __init__(self):
		self.run_method = RunMethod()
		self.data = GetData()
		self.com_util = CommonUtil()
		self.send_mai = SendEmail()


	# 程序执行
	def go_on_run(self):
		#结果
		res = None
		#通过率
		pass_count = []
		#失败率
		fail_count = []
		#获取case个数（获取有数据的单元格行）
		rows_count = self.data.get_case_lines()
		#循环判断要执行的case,跳过第一行标题开始循环
		for i in range(1,rows_count):
			#获取是否执行
			is_run = self.data.get_is_run(i)
			# print is_run
			# #判断is_run的值为true时执行
			if is_run:
					# print i
				#获取url
				url = self.data.get_request_url(i)
				# print url
				#获取请求类型
				method = self.data.get_request_method(i)
				# print method
				#获取数据
				data = self.data.get_request_data(i)
				# print data
				expect = self.data.get_expect_data(i)
				#获取header(默认demo)
				# header = self.data.demo_header()
				#获取excel中指定header
				header = self.data.is_header(i)
				# print header
				#获取依赖数据
				depend_case = self.data.is_depend(i)
				#判断是否需要依赖数据
				if depend_case != None:
					self.depend_data = DependentData(depend_case)
					#获取依赖的响应数据
					depend_response_data = self.depend_data.get_data_for_key(i)
					#获取依赖key
					depend_key = self.data.get_depend_field(i)
					#将获取到的依赖case响应数据赋值给依赖key
					request_data[depend_key] = depend_response_data
				#获取响应数据
				res = self.run_method.run_main(method,url,data,header)
				# print res
				#打印结果并转码为字符串类型
				# print res.text.encode('unicode-escape').decode('string_escape')

				#判断返回结果与预期结果比对
				if self.com_util.is_contain(expect,res):
					self.data.write_result(i, 'pass')
					#成功率统计
					pass_count.append(i)
				else:
					self.data.write_result(i, res)
					#失败率统计
					fail_count.append(i)
		#将比对出的结果写入邮件并发送
		# self.send_mai.send_mail(['2848958229@qq.com'], "第一封测试报告邮件", "此次共运行接口个数为：%s，通过个数为：%s，失败个数为：%s，通过率为：%s，失败率为：%s。"%(count_num,pass_num,fail_num,pass_result,fail_result))
		# self.send_mai.send_main(pass_count, fail_count)



				
if __name__ == '__main__':
	run = RunTest()
	run.go_on_run()

	