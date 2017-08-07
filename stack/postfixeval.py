############################
# postfix evaluation using stack(singlely linked list)
############################

###123*+5-

import sys

class stack:

    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
    
    def push(self,data=None,next=None):
        global head
        temp=stack()
        temp.data=data
        self.next=temp
        head=temp
        return head
        
    def pop(self,top=None):
        global head
        if top==self:
            return top.data
        else:
            while self.next is not top and self.next:
                self=self.next  
        self.next=None
        head=self
        return top.data
              
#####################
# main()
#####################

postfix = list(sys.argv[1])
exp=['+','-','*','/']
head=stack(postfix[0])
bottom=head #used for pop
for i in range(1,len(postfix)):
    if postfix[i] in exp:
        item1=int(bottom.pop(head))
        item2=int(bottom.pop(head))
        if postfix[i] == "+":
            head=head.push(item2 + item1)
        if postfix[i] == "-":
            head=head.push(item2 - item1)
        if postfix[i] == "*":
            head=head.push(item2 * item1)
        if postfix[i] == "/":
            head=head.push(item2 / item1)     
    else:
        head=head.push(postfix[i])
print    
print "Expression evaluates to : ", head.data
print
    

    
    
 
