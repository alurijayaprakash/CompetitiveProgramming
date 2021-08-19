# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

import math
def getDistance(x1, y1, x2, y2):
	return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# print(getDistance(-2, -3, -4, 4))

def assertAlmostEqual(x,y):
	return abs(x-y) < 10**-9

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	d1 = getDistance(x1, y1, x2, y2)
	d2 = getDistance(x2, y2, x3, y3)
	d3 = getDistance(x3, y3, x1, y1)
	dlist = [d1, d2, d3]
	# print(dlist)
	dlist.sort()
	# print(dlist)
	if (assertAlmostEqual((dlist[2])**2, ((dlist[0])**2 + (dlist[1])**2))):
		return True
	return False

# print(isrighttriangle(13, -1, -9, 3, -3, -9))
