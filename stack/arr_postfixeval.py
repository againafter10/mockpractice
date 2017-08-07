############################
# postfix evaluation using stack (Array)
############################

###123*+5-

import sys
 
        
#####################
# main()
#####################

postfix = list(sys.argv[1])
exp=['+','-','*','/']
stack=[]
stack.append(postfix[0])
stack.append(postfix[1])
print stack
for i in range(2,len(postfix)-1):
    if postfix[i] in exp:
        #pop 2 items
        print postfix[i]
        item1,item2=postfix[i-1],postfix[i-2]
        print "#################"
        print item1,item2
        print"###################"
        #stack.remove[i-1]
        #stack.remove[i-2]
        #stack.pop(i)
        #stack.pop(i)
        print stack
        print "*" *6
        print
        print
        if data == "+":
            print ("evaluating +")
            stack.append(item1+item2)
            print stack
        if data == "-":
            print ("evaluating -")
            stack.append(item1-item2) 
            print stack
        if data == "*":
            print ("evaluating *")
            stack.append(item1*item2)
            print stack
        if data == "/":
            print ("evaluating /")
            stack.append(item1/item2)
            print stack
        i+=1
            

            
print stack[0]


