#coding:utf-8
import requests
import json
class RunMethod:
	
	#post请求
	def post_main(self,url,data,header=None):
		res = None
		if header !=None:
			res = requests.post(url=url,data=data,headers=header)
		else:
			res = requests.post(url=url,data=data)
		#不要修改返回出去的类型，会影响预期结果的比对
		return res.json()

	#get请求
	def get_main(self,url,data=None,header=None):
		res = None
		if header !=None:
			res = requests.get(url=url,data=data,headers=header)
			# print res.status_code
		else:
			res = requests.get(url=url,data=data)
			# print res.status_code
		#不要修改返回出去的类型，会影响预期结果的比对
		return res.json()
		# return res
	
	def run_main(self,method,url,data=None,header=None):
		res = None
		if method == 'post':
			res = self.post_main(url,data,header)
		else:
			res = self.get_main(url,data,header)
		#不要修改返回出去的类型，会影响预期结果的比对
		return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=4)
		# return res

	






if __name__=='__main__':		#入口
	url = 'http://192.168.1.11:8050/auth/loginconfigs?lpm=3333.v2.4.2'	#将地址存入url键
	data = {  # 将参数存入data字典
		"username": "sadasjkdhjka",
		"mobile": "2134890887654",
		"cart": "11"
	}

	headers={
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate',
		'Accept-Language':'zh-CN,zh;q=0.9',
		'Cache-Control':'max-age=0',
		'Host':'192.168.1.11:8050',
		'Proxy-Connection':'keep-alive',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
	}

	
	run =RunMethod()

	res = run.run_main('POST',url,data,headers)

	print res