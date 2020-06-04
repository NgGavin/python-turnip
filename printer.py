"""
Created by: Gavin Ng
Read README for more information about python-turnip in general and its associated files
"""
import math


def fileprinter(buy_price, cycleoutput, cycleconverter):
	print("{:15}|".format("Minimum Values"),end="")
	for i in cycleoutput[0]:
		if i != cycleoutput[0][-1]:
			print("{:^12}|".format(math.ceil(i)),end="")
		else:
			print("{:^12}|".format(math.ceil(i)))
	print("_"*13*len(cycleoutput[0]),end="")
	print("_"*16)
	print("{:15}|".format("Maximum Values"),end="")
	for i in cycleoutput[1]:
		if i != cycleoutput[1][-1]:
			print("{:^12}|".format(math.ceil(i)),end="")
		else:
			print("{:^12}|".format(math.ceil(i)))
	print("_"*13*len(cycleoutput[0]),end="")
	print("_"*16)
	print("{:15}|".format("12 Hour Cycle"),end="")
	for i in cycleconverter:
		print("{:^12}|".format(i),end="")