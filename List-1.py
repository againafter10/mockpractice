'''
#####################################
# List-1
#####################################
#####################################
'''
'''
#####################################
# 1)  first_last6
#####################################

Given an array of ints, return True if 6 appears as either the first or last element in the array. 
The array will be length 1 or more.

'''
'''
def first_last6(nums):
    if ( nums[0] == 6 or nums[len(nums)-1]==6 ):
        return True
    else:
        return False
print(first_last6([13, 6, 1, 2, 3]))     

'''
'''
#####################################
# 2)  same_first_last 
#####################################

Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

'''
'''
def same_first_last(nums):
    if ( nums[0] == nums[len(nums)-1] )and len(nums) >= 1: 
        return True
    else:
        return False
    
print(same_first_last([1, 2, 3, 1]))

'''
'''
#####################################
# 3)  make_pi  
#####################################

Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

'''
'''
def make_pi():
    a= [3,1,4]
    return a
print(make_pi())
'''
'''
#####################################
# 4) common_end   
#####################################

Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element.
Both arrays will be length 1 or more.

'''
'''
def common_end(a, b):
    if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
        return True
    else:
        return False

print(common_end([5,1, 2, 3], [5,7, 3,6]))
'''
'''
#####################################
# 5) sum3 
#####################################

Given an array of ints length 3, return the sum of all the elements.

'''
'''
def sum(nums):
    return nums[0] + nums[1] + nums [2]

print(sum([2,3,4]))

'''
'''
#####################################
# 6) rotate_left3 / left rotate a list
#####################################

Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

'''
'''
def rotate_left3(nums):
    temp=nums[0]
    #for i in xrange(len(nums)-1,-1,-1): #reverse prinintg of the array
    for i in xrange(1,len(nums)):
        nums[i-1] = nums[i]
    nums[len(nums)-1]=temp
    return(nums)
        
print(rotate_left3([7, 45, 6,94,67,89]))

'''
'''
#####################################
# 7) reverse3 / reverse a list
#####################################

Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

'''
'''
def reverse3(nums):
    return nums[::-1]
print(reverse3([13, 25, 43]))
'''
'''
#####################################
# 8) max_end3 
#####################################

Given an array of ints length 3, figure out which is larger, the first or last element in the array,
and set all the other elements to be that value. Return the changed array.

'''
'''
def max_end3(nums):
    if nums[0] > nums[len(nums)-1]:
        big=nums[0]
    else:
        big=nums[len(nums)-1]
    for i in xrange(0,len(nums)):
        nums[i]=big
    return nums

print(max_end3([23, 11, 0]))

'''
'''
#####################################
# 9) sum2 
#####################################

Given an array of ints, return the sum of the first 2 elements in the array. 
If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

'''
'''
def sum2(nums):
    if len(nums)==0:
        return 0
    if len(nums)==1:
        return nums[0]
    
    else:
        return nums[0] + nums[1]

print(sum2([11]))

'''
'''
#####################################
# 10) middle_way 
#####################################

Given 2 int arrays, a and b, each length 3, 
return a new array length 2 containing their middle elements.

'''
'''
def middle_way(a, b):
    return [a[len(a)//2],b[len(a)//2]]
print(middle_way([5, 2, 9], [1, 4, 5]))
'''
'''
#####################################
# 11) make_ends 
#####################################

Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.

'''
'''
def make_ends(nums):
    return [ nums[0],nums[len(nums)-1]]

print(make_ends([7, 7, 4,6,2]))
'''
'''
#####################################
# 12) has23 
#####################################

Given an int array length 2, return True if it contains a 2 or a 3.


'''
'''
def has23(nums):
    if nums[0] == 2 or nums[1]== 2 or  nums[0] == 3 or nums[1]== 3:
        return True
    else:
        return False

print(has23([6, 3]))
'''