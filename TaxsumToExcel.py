#!/usr/local/bin/python3
##############################################
#Lillian Jensen, Robert Britton, MSU
##############################################

"""
Importing modules
"""

import openpyxl as px
import os
 
wb = px.workbook.Workbook
loadwb = px.load_workbook

book = loadwb("ERIN_Strains.xlsx")
sheet = book.active
tax = open("11514.trim.good.filter.pds.wang.taxonomy", 'r')

myDic = {}

for line in tax:
	myDic[line.split()[0]]=line.split()[1]
	
for row in sheet.range('A2::'):
	for cell in row:
		while cell.value != None:
			
