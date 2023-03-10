#!/usr/local/bin/python3
##############################################
#Lillian Jensen, Robert Britton, MSU
##############################################

f = open("ERIN_New_Isolates_30314_926R.multiBR_clindaout.trim.fasta", 'r')

l = []

for line in f:
	linelist = line.split(" ")
	again = linelist.split(" ")
	if linelist[0] == '>':
		l.append(line)
		
print(l)
