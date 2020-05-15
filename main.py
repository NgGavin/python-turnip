"""
Created by: Gavin Ng
Read README for more information about python-turnip in general and its associated files
"""

# File Imports
import trends.py
import printer.py

# Setup for Cycles
cycleconverter = ["Monday AM","Monday PM","Tuesday AM","Tuesday PM","Wednesday AM","Wednesday PM","Thursday AM","Thursday PM","Friday AM","Friday PM","Saturday AM","Saturday PM"]
cyclepoints = {"Monday AM" : 0,"Monday PM" : 0,"Tuesday AM" : 0,"Tuesday PM" : 0,"Wednesday AM" : 0,"Wednesday PM" : 0,"Thursday AM" : 0,"Thursday PM" : 0,"Friday AM" : 0,"Friday PM" : 0,"Saturday AM" : 0,"Saturday PM" : 0,}
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
for cycle in range(11):
	cycleprompt = input("Do you know the buy price of "+cycleconverter[cycle]+"? (y/n)")
	if cycleprompt.casefold() == 'y':
		cyclepoints[cycleconverter[cycle]] = int(input("What is the buy price of "+cycleconverter[cycle]+"?"))
	elif cycleprompt.casefold() == 'n':
		break
	else:
		print("Invalid input. Printing data...\n")
		break

# Cycle Datapoint Verification + Benchmark
print("These are the datapoints you have provided:")
print("\nInitial Buy Price of",buy_price,"\n")
for cycle in cyclepoints.keys():
	if cyclepoints[cycle] == 0:
		break
	else:
		print(cycleconverter[cycleconvertercounter]," = ",cyclepoints[cycle])
	cycleconvertercounter += 1
print("\n")

# Trend Determinatior Using Initial Buy Price and Cycle Datapoints
trendtype = trends.trendanalysis(buy_price,cyclepoints)

# Range Output According to Trend Type
if trendtype == 'random':
	cycleoutput = trends.random(cyclepoints)
elif trendtype == 'decreasing':
	cycleoutput = trends.decreasing(cyclepoints)
elif trendtype == 'small_spike':
	cycleoutput = trends.small_spike(cyclepoints)
elif trendtype == 'large_spike':
	cycleoutput = trends.large_spike(cyclepoints)

