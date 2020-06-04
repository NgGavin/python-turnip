"""
Created by: Gavin Ng
Read README for more information about python-turnip in general and its associated files
"""


def fileprinter(buy_price, cycleoutput, cycleconverter):
	print("Minimum Values |",end="")
	for i in cycleoutput[1]:
		print("{:9}|".format(i),end="")
	print("_"*2*len(cycleoutput[1]))
	print("Maximum Values |",end="")
	for i in cycleoutput[2]:
		print("{:9}|".format(i),end="")
	print("_"*2*len(cycleoutput[2]))
	print("12 Hour Cycle |",end="")
	for i in cycleconverter:
		print("{:9}|".format(i),end="")