############################
# heap sort
###########################

# Heapsort can be thought of as an improved selection sort: 
# it divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element and moving that to the sorted region
# The improvement consists of the use of a heap data structure rather than a linear-time search to find the maximum.
# Heapsort is an in-place algorithm, but it is not a stable sort.
# worst-case O(n log n) runtime. 

# Usage python heap.py "<<space separated list of numbers>>"
# 
import sys
global numlist

def swap(i, j):                    
    numlist[i], numlist[j] = numlist[j], numlist[i] 
    
def heapify(end,i):   
    l=2 * i + 1 
    r=2 * (i + 1)   
    max=i   
    if l < end and numlist[i] < numlist[l]:   
        max = l   
    if r < end and numlist[max] < numlist[r]:   
        max = r   
    if max != i:   
        swap(i, max)   
        heapify(end, max) 
        
def heap(numlist):     
    end = len(numlist)   
    start = end // 2 - 1
    for i in range(start, -1, -1):   
        heapify(end, i)   
    for i in range(end-1, 0, -1):   
        swap(i, 0)   
        heapify(i, 0) 
        
############################
# main()
############################

numlist= sys.argv[1]
numlist = numlist.split()
print "Unsorted list is: " , numlist
print
#numlist=heap(numlist)
heap(numlist)
print
print "Sorted list is : " , numlist 
