#coding:utf-8

import xlrd

class OperationExcel:
	def __init__(self,file_name=None, sheet_id=None):
		#有传文件时调用传的
		if file_name:
			self.file_name = file_name
			self.sheet_id = sheet_id
		#没有时调用指定的
		else:
			self.file_name = '../dataconfig/case2.xlsx'
			self.sheet_id = 0
		self.data = self.get_data()
	#获取sheets的内容
	def get_data(self):
		data = xlrd.open_workbook(self.file_name)
		tables = data.sheets()[self.sheet_id]
		return tables

	#获取单元格的行数
	def get_lines(self):
		tables = self.data
		return tables.nrows

	#获取某一个单元格的内容
	def get_cell_value(self,row,col):
		return self.data.cell_value(row,col)

if __name__ == '__main__':
	opers = OperationExcel()
	# print opers.get_lines()
	print opers.get_cell_value(0,9)