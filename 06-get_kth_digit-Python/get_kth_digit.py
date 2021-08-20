# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	digit = str(abs(digit))
	lendigit = len(digit)
	print("digit is", digit, lendigit, k)
	if (lendigit <= k):
		return 0
	return int(digit[lendigit-k-1])

print(fun_get_kth_digit(-789,3))