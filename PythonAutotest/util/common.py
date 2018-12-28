#coding:utf-8
import hashlib
import time
class CommonUtil:
	global TimeStamp

	#打印当前时间戳(毫秒)
	TimeStamp = int(time.time() * 1000)


	def is_contain(self,str_one,str_two):
		'''
		判断一个字符串是否在另一个字符串中
		str_one:查找的字符串
		str_two:被查的字符串
		'''
		flag = None
		#判断字符串类型
		if str_one in str_two:
			flag = True
		else:
			flag = False
		return flag

	def is_equal_dict(self,dict_one,dict_two):
		'''
		判断两个字典是否相同
		'''
		if isinstance(dict_one,str):
			dict_one = json.loads(dict_one)
		if isinstance(dict_two,str):
			dict_two = json.loads(dict_two)
		cmp(dict_one,dict_two)


	def is_list(self,list_one,list_two):
		self.list_one = ['xiaoWang','xiaoHua']
		self.list_two = ['xiaoWang','xiaoZhang','xiaoHua']
		if list_one in list_two:
			print('true')
		else:
			print("false")


	#签名串，需要安装hashlib插件
	def md5_key(self,OrgID,Version):
	    hash = hashlib.md5()
	    ef_key = OrgID +"|"+ str(TimeStamp) +"|"+ Version +"|"+"efortune"
	    hash.update(ef_key.encode("utf-8"))
	    return hash.hexdigest()

	#13位时间戳
	def time13(self):
		return TimeStamp



if __name__ == '__main__':
	md = CommonUtil()
	a= md.md5_key('org01','v1.0')
	b= md.time13()
	print(a)
	print(b)

