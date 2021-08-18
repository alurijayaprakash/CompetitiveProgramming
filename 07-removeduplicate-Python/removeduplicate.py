# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	list1 = list(text)
	list2 = []
	for i in list1:
		if i not in list2:
			list2.append(i)
	result = "".join(list2)
	return result
print(removeduplicate("JavaPython"))