# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	
	if n < 0:
		n = abs(n)
		flag = True
	else:
		flag = False
	numstr = str(n)
	numlen = len(str(n))
	print(flag, numstr, numlen)
	if k == numlen:
		tempnum =  int(str(d) + numstr)
		if flag:
			return -(tempnum)
		return tempnum
	else:
		if k == 0:
			return int(numstr[:2] + str(d))
		if k == 1:
			return int(numstr[:1] + str(d) + numstr[numlen-1])
		if k == 2:
			return int(str(d) + numstr[1:])


# print(fun_set_kth_digit(-468, 3, 1))