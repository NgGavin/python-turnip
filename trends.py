"""
Created by: Gavin Ng
Read README for more information about python-turnip in general and its associated files
"""

# Variable Setup for Trend Analysis
trendinterim = []
increasing1, decreasing1, increasing2, decreasing2, increasing3, decreasing3 = None, None, None, None, None, None
previousloop = "" # ('0' == increase, '1' == decrease)

# Variable Setup for Trend Output
cycleoutput = ""


# Determine the Trend Type
def trendanalysis(cyclepoints):
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
		elif trendinterim[previous] > trendinterim[current]:
			decreasing1 += 1
			previousloop += '1'
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
	trendtype = None #Placeholder
	return trendtype


# Decreasing Trend Type
def decreasing(cyclepoints):
	return cycleoutput


# Random Trend Type
def random(cyclepoints):
	return cycleoutput


# Small Spike Trend Type
def small_spike(cyclepoints):
	return cycleoutput


# Large Spike Trend Type
def large_spike(cyclepoints):
	return cycleoutput
