#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""An array A[1..n] is said to have a majority element if more than half of its entries are the same.
Given: A positive integer k≤20, a positive integer n≤104, and k arrays of size n containing positive
	integers not exceeding 105.
Return: For each array, output an element of this array occurring strictly more than n/2 times if such 
	element exists, and "-1" otherwise. """

from collections import Counter

def majority_element(array):


	"""method 1 uses sorted(). the majority element in a sorted array 
	will occupy the midpoint index in an array"""

	array = sorted([int(i) for i in array.split()])

	length = len(array)		#get length of array, initiate array indexing
	
	if length % 2 ==0:
		half = length//2

	else:
		half = length//2 



	# candidate1 = []  #empty list to hold the candidate number

	# #splitting numerical string into list of integers, sorting the 
							
	# for i in array:
	# 	if array[half] > half:
	# 		print array[half]
	# 	else:
	# 		print -1		#list and storing the sorted list into an variable
	
	# n = array[length/2]
	# print n

	# for i in array: 	#start loop through array
	# 	print array[majority]
		  
	
		# if array.count(n) > majority:  #checking for interger that occupies midpoint index
		# 	candidate1.append(n)  #appends integer to candidate1 

		# if len(candidate1) == 0: # if loop doesn't detect majority element, append -1 to candidate variable
		# 	candidate1.append(-1)

		print candidate1
	

	"""method 2: Uses python module Counter() from collections to count all instances of i in array, 
	and then compare instaces of i to length/2
	"""

	counted = Counter(array).most_common(1) #create variable that holds list of tuples  
					#(array integer, integer count)., ,
	
	candidate = []#create variable to hold candidate for majority element
	
	for key, value in counted:			# loops through keys and values of tuples
		if value > length/2:			#if integer count > than more than half of length of array,
			candidate.append(key)		#loop will append array's integer to candidate variable
		
	if len(candidate) == 0:				#if no majority element is found, append -1
		candidate.append(-1)

	print candidate


# assert majority_element("4 8") is True
majority_element("5 5 5 5 5 5 5 5")
majority_element("8 7 7 7 1 7 3 7")
majority_element("7 1 6 5 10 100 1000 1")
majority_element("5 1 6 7 1 1 10 1")


#sample data for majority element problem.
# 4 8
# 5 5 5 5 5 5 5 5
# 8 7 7 7 1 7 3 7
# 7 1 6 5 10 100 1000 1
# 5 1 6 7 1 1 10 1

#output: 5 7 -1 -1







