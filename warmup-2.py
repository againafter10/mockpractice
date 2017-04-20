''' 
#####################################
#####################################
# warmup-2
#####################################
#####################################

#####################################
# 1) string_times 
#####################################

Given a string and a non-negative int n, 
return a larger string that is n copies of the original string.

'''
'''
def string_times(str, n):
    return str *n
print(string_times('Hi',0))

'''
#####################################
#####################################

'''
#####################################
# 2) front_times 
#####################################

Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

'''
'''

def front_times(str, n):
    if len(str)<3:
        return str * n
    else:
        return str[:3] * n

print(front_times('Abc',0))

'''
'''
#####################################
# 3) string_bits 
#####################################

Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

'''
'''
def string_bits(str):
    return str[::2]

print(string_bits('Her')) 
'''

'''
#####################################
# 4) string_splosion 
#####################################

Given a non-empty string like "Code" return a string like "CCoCodCode".

'''
'''
def string_splosion(str):
    new_str=""
    for i in range(1,len(str)+1):
            new_str=new_str + str[:i] 
    return(new_str)
print(string_splosion('Code'))

'''
'''
#####################################
# 5) last2 
#####################################

Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

'''
''' 
def last2(str):
  # Screen out too-short string case.
  if len(str) < 2:
    return 0
  
  # last 2 chars, can be written as str[-2:]
  last2 = str[len(str)-2:]
  count = 0
  
  # Check each substring length 2 starting at i
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count

print(last2('xaxxaxxxxxxxaxx'))

''' 

'''
#####################################
# 6) array_count9 
#####################################

Given an array of ints, return the number of 9's in the array.


'''
'''
def array_count9(nums):
    count=0
    for i in nums:
        if  i == 9:
            count += 1
    return count
print(array_count9([1, 9, 9, 3, 9]))

'''
'''
#####################################
# 7) array_front9 
#####################################

Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

'''
'''
def array_front9(nums):
    count=1
    for i in nums:
        
        if i == 9:
            return True
        else:
            if count==4:
                return False
            else:
                count += 1
                continue
    return False

print(array_front9([ 2, 3, 4]))
'''
'''
#####################################
# 8) array123
#####################################

Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

'''
'''
def array123(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

print(array123([1, 1, 2, 3, 1]))

'''
'''

#####################################
# 9) string_match 
#####################################

Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

'''

def string_match(a, b):
# Figure which string is shorter.
    shorter = min(len(a), len(b))
    count = 0
  
    # Loop i over every substring starting spot.
    # Use length-1 here, so can use char str[i+1] in the loop
    for i in range(shorter-1):
        a_sub = a[i:i+2]
        b_sub = b[i:i+2]
        if a_sub == b_sub:
            count = count + 1

    return count

print(string_match('xxcaazz', 'xxbaaz'))