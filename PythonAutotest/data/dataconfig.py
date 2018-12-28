#coding:utf-8

class global_var:
	"""docstring for global_var"""
	#case_id
	Id = "0"
	name = "1"
	url ="2" 
	run = "3"
	request_way ="4"
	header = "5"
	case_depend = "6"
	data_depand ="7"
	field_depand = "8"
	data = "9"
	expect = "10" 
	result = "11"


#获取caseid
def get_id():
	return global_var.Id

def get_name():
	return global_var.name


def get_url():
	return global_var.url

def get_run():
	return global_var.run

def get_req_way():
	return global_var.request_way

def get_header():
	return global_var.header

def get_case_depend():
	return global_var.case_depend

def get_data_depend():
	return global_var.data_depand

def get_field_depend():
	return global_var.field_depand

def get_data():
	return global_var.data

def get_expect():
	return global_var.expect

def get_result():
	return global_var.result

def get_header_value():
	
	header = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate',
		'Accept-Language':'zh-CN,zh;q=0.9',
		'Cache-Control':'max-age=0',
		'Host':'192.168.1.11:8050',
		'Proxy-Connection':'keep-alive',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
	}
	return header
#携带安全密钥的请求头
def get_header_value_load():
	securit_key = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOiJqYWRtaW4xIiwiT3JnSUQiOiJvcmcwMDEiLCJDbGllbnRJUCI6IjE5Mi4xNjguMS44OSIsImlhdCI6MTU0NTk3NDc2NH0.lMWySIwUAvYb5W8pVWHJWPjwWHbPx5Wb2345vGq7Zjo"
	header = {
		"Host":"192.168.1.11:8050",
		"Connection":"keep-alive",
		"Accept":"application/json",
		"Authorization":securit_key,
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
		"Content-Type":"application/json",
		"Referer":"http://192.168.1.11:8050/monitors",
		"Accept-Encoding":"gzip, deflate",
		"Accept-Language":"zh-CN,zh;q=0.9"
	}

	return header