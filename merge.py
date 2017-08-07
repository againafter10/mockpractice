############################
# merge sort
###########################

# this scales well to very large lists, because its worst-case running time is O(n log n).
# It is also easily applied to lists, not only arrays, as it only requires sequential access, not random access. 
# However, it has additional O(n) space complexity, and involves a large number of copies in simple implementations
# First divide the list into the smallest unit (1 element), 
# then compare each element with the adjacent list to sort and merge the two adjacent lists. Finally all the elements are sorted

#Usage python merge.py "<<space separated list of numbers>>"
# python merge.py "12 34 1 44 56 23 12 45 -45 77 88 77"


import sys
  
def merge(left, right):
	if not len(left) or not len(right):
		return left or right

	result = []
	i, j = 0, 0
	while (len(result) < len(left) + len(right)):
		if left[i] < right[j]:
			result.append(left[i])
			i+= 1
		else:
			result.append(right[j])
			j+= 1
		if i == len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break 

	return result

def mergesort(numlist):
	if len(numlist) < 2:
		return numlist

	middle = len(numlist)/2
	left = mergesort(numlist[:middle])
	right = mergesort(numlist[middle:])

	return merge(left, right)
"""
if __name__ == "__main__":
	print mergesort([3,4,5,1,2,8,3,7,6])

"""
############################
# main()
############################

numlist= sys.argv[1]
numlist = numlist.split()
print "Unsorted list is: " , numlist
print
numlist=mergesort(numlist)
print
print "Sorted list is : " , numlist 
