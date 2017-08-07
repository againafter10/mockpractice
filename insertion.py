############################
# insertion sort
###########################

# The algorithm consists of inserting one element at a time into the previously sorted part of the array
# can use any sorting to sort the intermediate list
# complexity O(n2)

# Usage python insertion.py "<<space separated list of numbers>>"
# python insertion.py "12 34 1 44 56 23 12 45 -45 77 88 77"


import sys

def insertion(numlist):
    for i in range(1, len(numlist)):
        j = i-1
        key = numlist[i]
        while (numlist[j] > key) and (j >= 0):
            
            numlist[j+1] = numlist[j]
            j -= 1
        numlist[j+1] = key

    return numlist
    
############################
# main()
############################

numlist= sys.argv[1]
numlist = numlist.split()
print "Unsorted list is: " , numlist
print
numlist=insertion(numlist)
print
print "Sorted list is : " , numlist 