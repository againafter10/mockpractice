############################
# quick sort
###########################

# Quicksort is a divide and conquer algorithm /partition sorting 
# to partition an array an element called a pivot is selected. All elements smaller than the pivot are moved before it and all greater elements are moved after it. 
# The lesser and greater sublists are then recursively sorted. 
# This yields average time complexity of O(n log n), with low overhead, and thus this is a popular algorithm. 

# Usage python quick.py "<<space separated list of numbers>>"
# python quick.py "12 34 1 44 56 23 12 45 -45 77 88 77"


import sys

def quick(numlist):
    less = []
    pivotList = []
    more = []
    if len(numlist) <= 1:
        return numlist
    else:
        pivot = int(numlist[0])
        for i in numlist:
            if int(i) < pivot:
                less.append(i)
            elif int(i) > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quick(less)
        more = quick(more)
        return less + pivotList + more
    
############################
# main()
############################

numlist= sys.argv[1]
numlist = numlist.split()
print "Unsorted list is: " , numlist
print
numlist=quick(numlist)
print
print "Sorted list is : " , numlist 
