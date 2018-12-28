#coding:utf-8
#coding:utf-8
import json
class OperationJson:

	def __init__(self,file_path=None):
		if file_path == None:
			self.file_path = '../dataconfig/data.json'
		else:
			self.file_path = file_path
		self.data = self.read_data()

	#读取json文件
	def read_data(self):
		with open(self.file_path) as fp:
			data = json.load(fp)
			return data

	#根据关键字获取数据
	def get_data(self,id):
		return json.dumps(self.data[id], ensure_ascii=False)

if __name__ == '__main__':
	opjson = OperationJson()
	print(opjson.get_data('test_07'))