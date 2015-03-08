
# An array A[1..n] is said to have a majority element if more than half of its entries are the same.
# Given: A positive integer k≤20, a positive integer n≤104, and k arrays of size n containing positive
# integers not exceeding 105.
# Return: For each array, output an element of this array occurring strictly more than n/2 times if such 
# element exists, and "-1" otherwise.



#sample data for majority element problem.
# 4 8
# 5 5 5 5 5 5 5 5
# 8 7 7 7 1 7 3 7
# 7 1 6 5 10 100 1000 1
# 5 1 6 7 1 1 10 1

#output: 5 7 -1 -1

def majority_element(array):

	array = "8 7 7 7 1 7 3 7"
	array = [int(i) for i in array.split()]
	length = len(array)

	print length

	count = []

	for i in array:
		count.append(array.count(i))
	







