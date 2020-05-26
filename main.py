"""
Created by: Gavin Ng
Read README for more information about python-turnip in general and its associated files
"""

# File Imports
import trends.py
import printer.py

# Setup for Cycles
cycleconverter = ["Monday AM","Monday PM","Tuesday AM","Tuesday PM","Wednesday AM","Wednesday PM","Thursday AM","Thursday PM","Friday AM","Friday PM","Saturday AM","Saturday PM"]
cyclepoints = {"Monday AM" : None,"Monday PM" : None,"Tuesday AM" : None,"Tuesday PM" : None,"Wednesday AM" : None,"Wednesday PM" : None,"Thursday AM" : None,"Thursday PM" : None,"Friday AM" : None,"Friday PM" : None,"Saturday AM" : None,"Saturday PM" : None}
cycleconvertercounter = 0

# Initial Buy Price Input
while True:
	try:buy_price = int(input("How much did you initially pay for each turnip? "))
	except ValueError:
		print("Please input a valid integer")
	if buy_price >= 90 and buy_price <= 110:
		break
	else:
		print("Please input a valid integer")

# Dictionary Populator
for cycle in len(cyclepoints):
	cycleprompt = input("Do you know the buy price of "+cycleconverter[cycle]+"? (y/n)")
	if cycleprompt.casefold() == 'y':
		while True:
			try: cyclepoints[cycleconverter[cycle]] = int(input("What is the buy price of "+cycleconverter[cycle]+"?"))
			except ValueError:
				print("Please input your turnip price in integer form")
			if cyclepoints[cycleconverter[cycle]] <= 660 and cyclepoints[cycleconverter[cycle]] > 9:
				break
			else:
				print("Invalid Input. It is impossible to have a turnip price less than 9 bells or over 660 bells")
	elif cycleprompt.casefold() == 'n':
		break
	else:
		print("Invalid input. Printing data...\n")
		break

# Cycle Datapoint Verification + Benchmark
print("These are the datapoints you have provided:")
print("\nInitial Buy Price of",buy_price,"\n")
for cycle in cyclepoints.keys():
	if cyclepoints[cycle] == None:
		break
	else:
		print(cycleconverter[cycleconvertercounter]," = ",cyclepoints[cycle])
	cycleconvertercounter += 1
print("\n")

# Trend Determinatior Using Initial Buy Price and Cycle Datapoints (WIP)
trendtype = trends.trendanalysis(buy_price,cyclepoints)

# Range Output According to Trend Type (WIP)
if trendtype == 'random':
	cycleoutput = trends.random(cyclepoints)
elif trendtype == 'decreasing':
	cycleoutput = trends.decreasing(cyclepoints)
elif trendtype == 'small_spike':
	cycleoutput = trends.small_spike(cyclepoints)
elif trendtype == 'large_spike':
	cycleoutput = trends.large_spike(cyclepoints)
elif trendtype == None:
	print("Inconclusive results")

# Generate Output Using printer.py (WIP)
printer.fileprinter(cycleoutput)