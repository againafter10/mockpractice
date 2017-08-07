############################
# bubble sort
###########################

# compares the first two elements, and if the first is greater than the second
#it swaps them.It continues doing this for each pair of adjacent elements to the end of the data set. 
#performance O(n2)

#Usage python bubble.py "<<space separated list of numbers>>"
import sys

def bubble(numlist):
    changed = True
    while changed:
        changed = False
        for i in range(len(numlist) - 1):
            if int(numlist[i]) > int(numlist[i+1]):
                print("swapping %s %s" %(numlist[i],numlist[i+1]))
                numlist[i], numlist[i+1] = numlist[i+1], numlist[i]
                changed = True
                print numlist
    return numlist
############################
# main()
############################

numlist= sys.argv[1]
numlist = numlist.split()
print "Unsorted list is: " , numlist
print
numlist=bubble(numlist)
print
print "Sorted list is : " , numlist 
