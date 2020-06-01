"""
Created by: Gavin Ng
Read README for more information about python-turnip in general and its associated files
"""

# Global Setup
global startincrease, startdecrease, increasing1, decreasing1, increasing2, decreasing2, increasing3, decreasing3
startincrease, startdecrease, increasing1, decreasing1, increasing2, decreasing2, increasing3, decreasing3 = None, None, None, None, None, None, None, None


# Determine the Trend Type
def trendanalysis(buy_price, cyclepoints):
	# Variable/List Setup
	trendinterim = []
	previousloop = "" # ('0' == increase, '1' == decrease)
	cycleconverter = ["Monday AM","Monday PM","Tuesday AM","Tuesday PM","Wednesday AM","Wednesday PM","Thursday AM","Thursday PM","Friday AM","Friday PM","Saturday AM","Saturday PM"]

	# Converts Dictionary Into A List For Analysis
	for cycle in cyclepoints.values():
		if cycle != None:
			trendinterim.append(cycle)

	# Increasing and Decreasing Pattern Sorter
	previous = 0
	for current in len(trendinterim):
		if trendinterim[previous] < trendinterim[current]:
			increasing1 += 1
			previousloop += '0'
			if increasing1 == 1 and decreasing1 == 0:
				startincrease = True
		elif trendinterim[previous] > trendinterim[current]:
			decreasing1 += 1
			previousloop += '1'
			if decreasing1 == 1 and increasing1 == 0:
				startdecrease = True
		elif trendinterim[previous] < trendinterim[current] and previousloop[-1] == '1' and increasing1 != None and decreasing1 != None:
			increasing2 += 1
			previousloop += '0'
		elif trendinterim[previous] > trendinterim[current] and previousloop[-1] == '0' and increasing1 != None and decreasing1 != None:
			decreasing1 += 1
			previousloop += '1'
		elif trendinterim[previous] < trendinterim[current] and previousloop[-1] == '1' and increasing1 != None and decreasing1 != None and increasing2 != None and decreasing2 != None:
			increasing3 += 1
			previousloop += '0'
		elif trendinterim[previous] > trendinterim[current] and previousloop[-1] == '0' and increasing1 != None and decreasing1 != None and increasing2 != None and decreasing2 != None:
			decreasing3 += 1
			previousloop += '1'
		previous = current - 1
	
	# Determine Trend Pattern Based Off Of Trend Phases
	decreasingtrend = None
	randomtrend = None
	small_spiketrend = None
	large_spiketrend = None
	
	# Decreasing
	if startdecrease == True and increasing1 == 0 and increasing2 == 0 and increasing3 == 0:
		decreasingtrend = True
	else:
		decreasingtrend = False

	# Random
	if (3 >= decreasing1 >= 2) and startdecrease == True and cyclepoints[cycleconverter[0]] in range(buy_price * .6, buy_price * .8001):
		randomtrend = True
	elif (3 >= decreasing1 >= 2) and startincrease == True and cyclepoints[cycleconverter[0]] in range(buy_price * .9, buy_price * 1.4001) and cyclepoints[cycleconverter[increasing1-1]] in range(buy_price * .6, buy_price * .8001):
		randomtrend = True
	else:
		randomtrend = False
	
	# Small Spike
	if (5 >= increasing1 >= 1) and increasing2 == 0 and increasing3 == 0 and decreasing3 == 0 and cyclepoints[cycleconverter[decreasing1 - 1]] in range(buy_price * .9, buy_price * 1.4001):
		small_spiketrend = True
	else:
		small_spiketrend = False

	# Large Spike
	if startdecrease == True and (7 <= decreasing1 >= 1) and decreasing2 == 2 and increasing1 == 3 and increasing2 == 0:
		large_spiketrend = True
	else:
		large_spiketrend = False
	
	# Return Trend Value
	if decreasingtrend == True and (randomtrend == False or randomtrend == None) and (small_spiketrend == False or small_spiketrend == None) and (large_spiketrend == False or large_spiketrend == None):
		trendtype = 'decreasing'
	elif randomtrend == True and (decreasingtrend == False or decreasingtrend == None) and (small_spiketrend == False or small_spiketrend == None) and (large_spiketrend == False or large_spiketrend == None):
		trendtype = 'random'
	elif small_spiketrend == True and (decreasingtrend == False or decreasingtrend == None) and (randomtrend == False or randomtrend == None) and (large_spiketrend == False or large_spiketrend == None):
		trendtype = 'small_spike'
	elif large_spiketrend == True and (decreasingtrend == False or decreasingtrend == None) and (randomtrend == False or randomtrend == None) and (small_spiketrend == False or small_spiketrend == None):
		trendtype = 'large_spike'
	else:
		trendtype = None
	return trendtype

def cyclesetup(buy_price, cyclepoints):
	# Variable Setup
	trendinterim = []
	minimumcycle = []
	maximumcycle = []
	# Converts Dictionary Into A List For Analysis
	for cycle in cyclepoints.values():
		if cycle != None:
			trendinterim.append(cycle)
		elif len(trendinterim) < 12:
			trendinterim.append(None)
	for i in trendinterim:
		minimumcycle.append(i)
		maximumcycle.append(i)
	return trendinterim, minimumcycle, maximumcycle

# Decreasing Trend Type
def decreasing(buy_price, cyclepoints):
	trendinterim, minimumcycle, maximumcycle = cyclesetup(buy_price, cyclepoints)
	counter = 0
	baserate = [trendinterim[0]/0.85,trendinterim[0]/0.9]
	for i in trendinterim:
		if i == None:
			minimumcycle.append(trendinterim[counter]-(baserate[0]*0.05))
			maximumcycle.append(trendinterim[counter]-(baserate[1]*0.03))
		counter += 1
	return minimumcycle,maximumcycle


# Random Trend Type
def random(buy_price, cyclepoints):
	trendinterim, minimumcycle, maximumcycle, cycleoutput= cyclesetup(buy_price, cyclepoints)
	counter = 0
	decreasingcounter = None
	baserate = [buy_price*0.6,buy_price*0.8]
	for i in trendinterim:
		if i == None:
			if startincrease:
				if i in range(increasing1 + decreasing1,increasing1 + decreasing1 + increasing2) or i in range(increasing1 + decreasing1 + increasing2 + decreasing2, increasing1 + decreasing1 + increasing2 + decreasing2 + increasing3):
					minimumcycle.append(buy_price*0.9)
					maximumcycle.append(buy_price*1.4)
				elif i in range(increasing1 + decreasing1 + increasing2, decreasing2):
					if decreasingcounter == True:
						minimumcycle.append(baserate[0])
						maximumcycle.append(baserate[1])
					else:
						minimumcycle.append(trendinterim[counter-1]-baserate[0]*.1)
						maximumcycle.append(trendinterim[counter-1]-baserate[0]*0.04)
					decreasingcounter = True
			elif startdecrease:
				if i in range(decreasing1,increasing1) or i in range(decreasing1 + increasing1 + decreasing2, increasing3):
					minimumcycle.append(buy_price*0.9)
					maximumcycle.append(buy_price*1.4)
				elif i in range(decreasing1 + increasing1, decreasing2):
					if decreasingcounter == True:
						minimumcycle.append(baserate[0])
						maximumcycle.append(baserate[1])
					else:
						minimumcycle.append(trendinterim[counter-1]-baserate[0]*.1)
						maximumcycle.append(trendinterim[counter-1]-baserate[0]*0.04)
					decreasingcounter = True
		counter += 1
	return cycleoutput


# Small Spike Trend Type
def small_spike(buy_price, cyclepoints):
	trendinterim, minimumcycle, maximumcycle, cycleoutput= cyclesetup(buy_price, cyclepoints)
	return cycleoutput


# Large Spike Trend Type
def large_spike(buy_price, cyclepoints):
	trendinterim, minimumcycle, maximumcycle, cycleoutput= cyclesetup(buy_price, cyclepoints)
	return cycleoutput


# Inconclusive Spike Trend Type
def inconclusive(buy_price, cyclepoints):
	trendinterim, minimumcycle, maximumcycle, cycleoutput= cyclesetup(buy_price, cyclepoints)
	for i in trendinterim:
		if i != None:
			minimumcycle.append(9)
			maximumcycle.append(660)
	return cycleoutput