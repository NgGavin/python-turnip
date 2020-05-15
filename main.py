"""
Read README for more information about python-turnip in general and its associated files
"""

cycleconverter = ["Monday AM","Monday PM","Tuesday AM","Tuesday PM","Wednesday AM","Wednesday PM","Thursday AM","Thursday PM","Friday AM","Friday PM","Saturday AM","Saturday PM"]
cyclepoints = {"Monday AM" : 0,"Monday PM" : 0,"Tuesday AM" : 0,"Tuesday PM" : 0,"Wednesday AM" : 0,"Wednesday PM" : 0,"Thursday AM" : 0,"Thursday PM" : 0,"Friday AM" : 0,"Friday PM" : 0,"Saturday AM" : 0,"Saturday PM" : 0,}

while True:
	try:buy_price = int(input("How much did you initially pay for each turnip? "))
	except ValueError:
		print("Please input a valid integer")
	if buy_price >= 90 and buy_price <= 110:
		break
	else:
		print("Please input a valid integer")

for cycle in range(11):
	while True:
		cycleprompt = input("Do you know the buy price of "+cycleconverter[cycle]+"? (y/n)")
		if cycleprompt == 'y' or cycleprompt == 'n':
			break
		else:
			print("Please input a valid response")
	if cycleprompt.casefold() == 'y':
		cyclepoints[cycleconverter[cycle]] = int(input("What is the buy price of "+cycleconverter[cycle]+"?"))
	elif cycleprompt.casefold() == 'n':
		break

