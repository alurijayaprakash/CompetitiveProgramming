# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	n = abs(n)
	prev = n % 10
	n = n // 10
	print(n,prev)
	while n != 0:
		rem = n % 10
		print(n,prev)
		if prev == rem:
			return True
		else:
			prev = rem
			n = n // 10
	return False

print(hasconsecutivedigits(14))