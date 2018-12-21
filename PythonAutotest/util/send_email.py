#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class SendEmail:
	#定义发件人
	global send_user
	#定义发件邮箱服务地址，需要先下载sendmail服务，然后在sendmail.ini中定义好
	global email_host
	#定义发件邮箱密码，qq邮箱从IMP中获取一下密码
	global password
	#定义附件
	global send_file

	send_user = '2511431965@qq.com'
	email_host = 'smtp.qq.com'
	password = 'uumnjokpuyrmdihb'
	send_file = None
	pass_list = []
	fail_list = []

	def send_mail(self,user_list,sub,content,send_file):
		#构建发件人
		user = "吉涛"+"<"+send_user+">"
		message = MIMEMultipart()
		#构建格式
		message.attach(MIMEText(content,'plain', 'utf-8'))
		#格式中主题
		message['subject'] = sub
		#格式中发件人
		message['From'] = user
		#格式中收件人
		message['To'] = ";".join(user_list)
		#发送附件
		#打开要发送的文件，请勿用中文命名文件
		send_file=open(r"E:/pythonworkspace/PythonAutotest/dataconfig/case2.xlsx",'rb').read()
		#定义发送后的附件文件名
		resultfilename = "results.xlsx"
		#构建附件格式编码
		text_attr = MIMEText(send_file, 'base64', 'utf-8')  
		text_attr["Content-Type"] = 'application/octet-stream'
		text_attr["Content-Disposition"] = 'attachment; filename=%s'%resultfilename
		message.attach(text_attr)
		#连接发送邮件服务
		server = smtplib.SMTP()
		server.connect(email_host)
		#传入邮箱账户及密码
		server.login(send_user,password)
		#发送邮件,内容需要重新编码
		server.sendmail(user,user_list,message.as_string())
		#关闭服务
		server.close()


	def send_main(self,pass_list,fail_list):
		#获取通过的和失败的case数并将结果转为float类型
		pass_num = float(len(pass_list))
		fail_num = float(len(fail_list))
		count_num = pass_num+fail_num
		#转化为百分比
		pass_result = "%.2f%%"%(pass_num/count_num*100)
		fail_result = "%.2f%%"%(fail_num/count_num*100)

		user_list = ['2848958229@qq.com']
		sub = "测试邮件"
		content = "此次共运行接口个数为：%s个，通过个数为：%s个，失败个数为：%s个，通过率为：%s，失败率为：%s，请查看附件中的详细测试报告中的【实际结果】字段中的返回结果，若全部通过，请忽略。"%(count_num,pass_num,fail_num,pass_result,fail_result)
		self.send_mail(user_list, sub, content,send_file)

if __name__ == '__main__':
	send = SendEmail()
	send.send_main([1,1,3],[4,5,6])