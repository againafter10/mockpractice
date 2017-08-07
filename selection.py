############################
# selection sort
###########################

# Selection sort is an in-place comparison sort. It has O(n2) complexity, making it inefficient on large lists

#Usage python selection.py "<<space separated list of numbers>>"
import sys

def selection(numlist):
    for i in range(len(numlist)-1):
        for j in range(i+1,len(numlist)):
            if int(numlist[i]) > int(numlist[j]):
                numlist[j]=int(numlist[i]) + int(numlist[j])
                numlist[i]=int(numlist[j]) - int(numlist[i])
                numlist[j]=int(numlist[j]) - int(numlist[i])
    return numlist
############################
# main()
############################

numlist= sys.argv[1]
numlist = numlist.split()
print "Unsorted list is: " , numlist
print
numlist=selection(numlist)
print "Sorted list is : " , numlist 
