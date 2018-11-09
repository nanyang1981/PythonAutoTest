#coding:utf-8
#导入json
import json
#打开文件login.json
# fp = open("../dataconfig/login.json")
# #读取文件
# data = json.load(fp)
# #输出读取指定内容
# print data['addcart']


class OperationJson:
	def __init__(self):
		self.data = self.read_data()

	#读取json文件
	def read_data(self):
		with open("../dataconfig/agent.json") as fp:
			data = json.load(fp)
			return data

	#根据关键字获取数据
	def get_data(self,id):
		return self.data[id]

if __name__ == '__main__':
	opjson = OperationJson()
	print opjson.get_data('demo2')