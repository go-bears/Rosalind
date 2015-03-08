#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""An array A[1..n] is said to have a majority element if more than half of its entries are the same.
Given: A positive integer k≤20, a positive integer n≤10*4, and k arrays of size n containing positive integers not exceeding 10*5.
Return: For each array, output an element of this array occurring strictly more than n/2 times if such element exists, and "-1" otherwise. """


#Hint: if an integer element occupies more than half of the index places, the element should occupy the array[n/2] position in the array or halfway mark after the array is sorted from min to max integers

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


#loop to turn set of individual arrays into lists of integers, this works

sorted_arrays = []

for single_array in num_arrays:
	sorted_arrays.append(sorted(map(int, single_array))) #map() applies the int() across the all the individual arrays as the loop runs.
			

#loop counts instances that the midpoint entry appears in the array"
candidate = []

#loops through singles arrays to find integer at n/2 position
for single in sorted_arrays:
	midpoint_entry = single[midpoint] 
	
	#loop through midpoint entry integers to count instances of midpoint entry
	c = 0
	for n in single:
		if midpoint_entry == n:
			c +=1

	# checks if instances of midpoint entry is majority element candidate
	if c > midpoint: 
		candidate.append(midpoint_entry)
	else:
		candidate.append(-1)

#strip commas out of output, Rosalind checker doesn't take commas generated by python's list
stripped = ', '.join(map(str, candidate)) #joins matched_index's integers as a single string
print stripped.replace(',', ' ') #replaces commas with spaces
