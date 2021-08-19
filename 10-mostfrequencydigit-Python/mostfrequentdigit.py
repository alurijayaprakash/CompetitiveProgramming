# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.
import math
def mostfrequentdigit(n):
	# your code goes here
	mylist = [int(i) for i in str(n)]
	mydict = dict()
	for i in mylist:
		if i in mydict:
			mydict[i] = mydict[i] + 1
		else:
			mydict[i] = 1
	print(mydict)
	minval = max(mydict.values())
	# valdata = [x for x in mydict.values() if x == minval]
	result = math.inf
	for a,b in mydict.items():
		if b == minval and a < result:
			result = a


	# print(valdata, result)
	return result


# print(mostfrequentdigit(26011))