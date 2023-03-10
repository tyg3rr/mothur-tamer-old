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

	for row in sheet.range(str('A1:B' + str(x))):   #making a list of well positions and ERIN names by reading the excel file
		for cell in row:
			lis1.append(cell.value)


	thedic = {}
	

	for i in range(0,len(lis1)):		#looking through the list, for the ith element in the list
		if i%2==0:						#if the ith element is even, make sure that single digit well positions 
			if len(lis1[i]) != 3:		#have a 0 in the middle, i.e A1 -> A01
				thedic[(lis1[i][-2] + '0' + lis1[i][-1])] = lis1[i+1]
			else:
				thedic[lis1[i]] = lis1[i+1]		#make a dictionary with odd elements as the keys and even elements as the values
		else:
			continue
	#print(thedic)  ##Debuging

	f = open(txt, 'r')		#opening the fasta file and creating an empty list
	alist = []
	
	for line in f:								#finding the lines in the file that begin with a '>', finding the well position,
		if line[0]=='>':					#using the well position in the dictionary to find the ERIN number, and changing the 
			for k in thedic.keys():			#title to '>ERIN_number'
				if k in line:
					line = '>' + str(thedic[k])
		alist.append(line)	
	
	f.close()
	
	g = open(txt, 'w')		#overwriting the old file with the new lines
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

"""
Talking to mothur to classify the sequences
"""

l1 = 'mothur "#summary.seqs(fasta='+ derp+ ');trim.seqs(fasta=' + derp + ', qfile=' + narf + ', qwindowaverage=20, qwindowsize=50, maxambig=0, maxhomop=8);summary.seqs(fasta=current);align.seqs(fasta=current, reference=silva.gold.align, flip=T);summary.seqs(fasta=current)"'
print(os.system(l1))
end = input("At which nucleotide position do you want your end parameter? This position screens your sequences such that 85% of them will end here: ")
l5 = 'mothur "#screen.seqs(fasta=' + fassa + '.trim.align, end=' + end + ', criteria=85, optimize=start);summary.seqs(fasta=current);filter.seqs(fasta=' + fassa + '.trim.good.align, vertical=T);summary.seqs(fasta=current);classify.seqs(fasta=' + fassa + '.trim.good.filter.fasta, template=trainset9_032012.pds.fasta, taxonomy=trainset9_032012.pds.tax, cutoff=80)"'
print(os.system(l5))
l6 = "open " + fassa + ".trim.good.filter.pds.wang.taxonomy"
print(os.system(l6))
