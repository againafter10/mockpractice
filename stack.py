############################
# Stack using arrays
############################

# create the stack

# print the stack
# add element to stack
# delete element to stack
# find element in stack

############################
############################
############################
l_stack=[]
data=raw_input("enter elements of stack,press enter to stop: ")
if data == "":
    print("empty stack:")
    quit()
while data:
    l_stack.append(data)
    data=raw_input("next stack element,press enter to stop: ")

#size=len(l_stack)

print("Elements as in stack are:")
for i in range(len(l_stack)-1,-1,-1):
    print l_stack[i]

d=int(raw_input("enter the stack position to delete"))
t_stack=l_stack[d+1:]
l_stack=l_stack[:d]
#l_stack=t_stack + l_stack
l_stack=l_stack + t_stack

print(l_stack)
        
        

        
