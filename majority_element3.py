#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""An array A[1..n] is said to have a majority element if more than half of its entries are the same.
Given: A positive integer k≤20, a positive integer n≤10*4, and k arrays of size n containing positive integers not exceeding 10*5.
Return: For each array, output an element of this array occurring strictly more than n/2 times if such element exists, and "-1" otherwise. """

from collections import Counter


#parsing text files data

with open('rosalind_maj.txt', 'r') as f: #open text as 
	integer_list = f.readlines()

dataset_features = integer_list[0].split() #the first line of dataset hold # of entries and length of a single array.

entries = int(dataset_features[0]) #total number of arrays in dataset

entry_length = int(dataset_features[1]) #total number of entries within a single array
midpoint = entry_length/2 #finds the n/2 value for the array. 

print entries, entry_length
print midpoint, "is the midpoint"


	#collect the individual arrays from dataset into variable arrays
raw_arrays = integer_list[1:entries +1]
	
	#loop to separate individual arrays

num_arrays =[]

for string_array in raw_arrays:	
	num_arrays.append(string_array.split())


print len(num_arrays)


#loop to turn set of individual arrays into lists of integers, this works

sorted_arrays = []

instances = []
candidate = []

final_candidates= []


for single_array in num_arrays:
	
	sorted_arrays.append(sorted(map(int, single_array))) #map() applies the int() across the all the individual arrays as the loop runs.
	
	counted = Counter(single_array).most_common(1) # Counter().most_common()finds most common element in an array and returns a tuple of (element, instances)
	counted = dict(counted) #converts tuple created by into dictionary
	

	string_candidate = counted.keys() #isolates "candidate" from dictionary in a variable
	num_candidate = int(', '.join(string_candidate)) #turns key from string to integer
	candidate.append(num_candidate)
	
	
	instance = counted.values() #isolates "instances" from dictionary, already is an integer
	
	instances.append(instance)

print len(instances)


for n in instances:
	n = int(n[0])
	
	if n > midpoint:
		
		final_candidates.append("candidate")

	else: 
		final_candidates.append(-1)


print type(n)

print type(midpoint)
print type(instances)

print final_candidates
print len(final_candidates)

# 		#finds the entry that is midpoint of the array
# 		midpoint_entry = single_array[midpoint] 
			

# 		#counts the number of instances the midpoint entry appears in the array.
# 		x = sorted_arrays.count(midpoint_entry), #"is the number of instances that the midpoint entry appears in the array"

# 	if x > midpoint:
# 		candidates_list.append(midpoint_entry)
# 	else:
# 		candidates_list.append(-1)

# print candidates_list

# #creates list of number values for a single arrray, this works
# array1 = sorted([int(j) for j in raw_arrays[2].split()])

# print array1






"""this section counts the most common value in an array, using Counter() function"""



#uses Counter() to find the most common value in the array & number of instances as a tuple of (value, instances)
