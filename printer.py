"""
Created by: Gavin Ng
Read README for more information about python-turnip in general and its associated files
"""
import math


def fileprinter(buy_price, cycleoutput, cycleconverter, cyclepoints):
	# Provided Values Display
	print("\n")
	print("{:15}|".format("Buy Price"),end="")
	print("{:^12}|".format(buy_price))
	print("_"*29)
	print("{:15}|".format("Provided Values"),end="")
	for i in cyclepoints.values():
		if i != None:
			print("{:^12}|".format(i),end="")
		else:
			print("{:^12}|".format("None"),end="")
	print("")
	print("_"*13*len(cyclepoints.values()),end="")
	print("_"*16)
	# Maximum Values
	print("{:15}|".format("Maximum Values"),end="")
	for i in cycleoutput[1]:
		if i != cycleoutput[1][-1]:
			print("{:^12}|".format(math.ceil(i)),end="")
		else:
			print("{:^12}|".format(math.ceil(i)))
	print("_"*13*len(cycleoutput[0]),end="")
	print("_"*16)
	# Average of Values
	print("{:15}|".format("Average Values"),end="")
	for i in range(len(cycleoutput[1])):
		if i != 11:
			print("{:^12}|".format(math.ceil((cycleoutput[0][i]+cycleoutput[1][i])/2)),end="")
		else:
			print("{:^12}|".format(math.ceil((cycleoutput[0][i]+cycleoutput[1][i])/2)))
	print("_"*13*len(cycleoutput[0]),end="")
	print("_"*16)
	# Minimum Values
	print("{:15}|".format("Minimum Values"),end="")
	for i in cycleoutput[0]:
		if i != cycleoutput[0][-1]:
			print("{:^12}|".format(math.ceil(i)),end="")
		else:
			print("{:^12}|".format(math.ceil(i)))
	print("_"*13*len(cycleoutput[0]),end="")
	print("_"*16)
	# 12 Hour Cycle Labels
	print("{:15}|".format("12 Hour Cycle"),end="")
	for i in cycleconverter:
		print("{:^12}|".format(i),end="")
	print("")
	print("_"*13*len(cycleoutput[0]),end="")
	print("_"*16)