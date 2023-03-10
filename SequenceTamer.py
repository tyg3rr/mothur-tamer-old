#!/usr/local/bin/python3
#Lillian Jensen, Robert Britton, MSU

"""
Importing modules
"""

import openpyxl as px

 
wb = px.workbook.Workbook
loadwb = px.load_workbook
 
"""
Taking user input and assigning variables
"""
slurp = input("Input the name of your excel database: ")
derp = input("Input the name of your fastA file: ")      
narf = input("Input the name of your qual file: ")
fassa = derp.split('.')[0]

"""
Counting how many samples there are in the excel reference
"""

book = loadwb(slurp)
sheet = book.active
count = 0                             
for row in sheet.range('A1:B96'):
		for cell in row:
			if cell.value != None:
				count +=1
num = int(count/2)


"""
Defining a function that has input a text file, an excel file, and a number.
The function uses the excel reference to cleanup the text file, and outputs it.
"""

def theFunction(txt, xlsx, x):
	book = loadwb(xlsx)
	sheet = book.active

	lis1 = []

	for row in sheet.range(str('A1:B' + str(x))):
		for cell in row:
			lis1.append(cell.value)


	thedic = {}
	

	for i in range(0,len(lis1)):
		if i%2==0:
			if len(lis1[i]) != 3:
				thedic[(lis1[i][-2] + '0' + lis1[i][-1])] = lis1[i+1]
			else:
				thedic[lis1[i]] = lis1[i+1]
		else:
			continue
	#print(thedic)  ##Debuging

	f = open(txt, 'r')
	alist = []
	
	for line in f:
		if line[0]=='>':
			for k in thedic.keys():
				if k in line:
					line = '>' + str(thedic[k])
		alist.append(line)	
	
	f.close()
	
	g = open(txt, 'w')
	for thing in alist:
		g.write(thing)
		g.write("\n")
		
	g.close()
	
	#g = open(txt,'r')          ##Debugging 
		

	#for line in g:		
		#print(line)
	
	#g.close()
	
	
"""
Calling the functions
"""		

theFunction(derp, slurp, num)
theFunction(narf, slurp, num)
