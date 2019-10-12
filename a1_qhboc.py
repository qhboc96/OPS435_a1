#!/usr/bin/env python3
#OPS435 Assignment 1 - Fall 2019
#Program: a1_qhboc.py
#Author: Quoc Hien Boc

import os
import sys

def usage():
	if ((len(sys.argv) != 4) and len(sys.argv) != 3): 
		print ('Usage: '+ sys.argv[0] + ' [--step] YYYYMMDD +/-n')
		exit()



def dbda(date,days):
	i = 0
	total = 0
	result = date
	if len(str(days)) == 10:
		valid_date(days)
		if date < days:
			while result < days:  
				total +=1
				result = after(result)
		elif date > days:
			while result > days:  
				total +=1
				result = before(result)
		print(total) 	

	else:	
		if int(days) > 0: 
			while i < int(days):  
				i += 1
				if sys.argv[1] == '--step':
					result = after(result)
					print(result)
				else:
					result = after(result)				

				
		elif int(days) < 0:  
			while i > int(days):
				i = i - 1
				if sys.argv[1] == '--step':
					result = before(result)
					print(result)
				else:
					result = before(result)			
				
		else:
			result = result

		if sys.argv[1] == '--step':
			print('', end='')
		else:
			print(result)



def days_in_mon(year_value):
	if leap_year(year_value):
		feb = 29
	else:
		feb = 28

	mon_max = { 1:31, 2:feb, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	return mon_max
    
def leap_year(year_value):
	if (year_value % 4 == 0):
		if (year_value % 100 == 0):
			if (year_value % 400 ==0):
				is_leapyear = True
			else:
				is_leapyear = False
		else:
			is_leapyear = True
	else:
		is_leapyear = False
    		
	return is_leapyear
    
def valid_date(var1):
	if (len(var1) != 10):   
		print("Error: wrong date entered")
		exit()
	else:
		year = int(var1[0:4])
		month = int(var1[5:7])
		day = int(var1[8:])
		mon_max = days_in_mon(year)

		if month not in mon_max.keys():
			print("Error: wrong month entered")
			exit()
		else:
			day_max = mon_max[month]
			if day not in range (1,day_max+1):    
				print("Error: wrong day entered")
				exit()


def after(today):
	valid_date(today)
	year = int(today[0:4])
	month = int(today[5:7])
	day = int(today[8:])
	mon_max = days_in_mon(year)
	af_day = day + 1
	
	if af_day > mon_max[month]: 
		af_day = 1
		month = month + 1
		if month > 12:
			month = 1
			year = year + 1

	next_date = str(year)+'/'+str(month).zfill(2)+'/'+str(af_day).zfill(2)
	return next_date
	
def before(today):
	valid_date(today)
	year = int(today[0:4])
	month = int(today[5:7])
	day = int(today[8:])
	mon_max = days_in_mon(year)
	bf_day = day - 1
	if bf_day == 0:
		month = month - 1
		if month == 0:
			year = year -1
			month = 12
			bf_day = 31
		else:
			bf_day = mon_max[month]

	previous_date = str(year)+'/'+str(month).zfill(2)+'/'+str(bf_day).zfill(2)
	return previous_date

if __name__ == "__main__":
	usage()
	if sys.argv[1] == '--step':
		date = sys.argv[2]
		days = sys.argv[3]
	else:
		date = sys.argv[1]
		days = sys.argv[2]

	dbda(date,days)
