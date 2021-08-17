# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
	lenhand = len(str(hand))
	x = hand // 10**(lenhand-1)
	hand = hand % 10**(lenhand-1)
	# print(hand)
	y = hand // 10**(lenhand-2)
	hand = hand % 10**(lenhand-2)
	z = hand // 10**(lenhand-3)
	return x,y,z


# print(handtodice(123))