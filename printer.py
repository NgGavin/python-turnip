"""
Created by: Gavin Ng
Read README for more information about python-turnip in general and its associated files
"""
import math


def fileprinter(buy_price, cycleoutput, cycleconverter):
	print(cycleoutput)
	print("{:15}|".format("Minimum Values"),end="")
	for i in cycleoutput[0]:
		print("{:^12}|".format(math.ceil(i)),end="")
	print("_"*9*len(cycleoutput[1]))
	print("{:15}|".format("Maximum Values"),end="")
	for i in cycleoutput[1]:
		print("{:^12}|".format(math.ceil(i)),end="")
	print("_"*9*len(cycleoutput[0]))
	print("{:15}|".format("12 Hour Cycle"),end="")
	for i in cycleconverter:
		print("{:^12}|".format(i),end="")