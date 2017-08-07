############################
# stack using singlely linked list
############################

###123*+5-

import sys
class stack:

    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
    
    def push(self,data=None,next=None):
        temp=stack()
        temp.data=data
        self.next=temp
        head=temp
        return head
        
    def pop(self,head=None):
        print head.data
        if head==self:
            pass
        else:
            while self.next is not head:
                self=self.next
            
        self.next=None
        head=self
        return head
        
        
        
    
        
#####################
# main()
#####################

postfix = list(sys.argv[1])
exp=['+','-','*','/']
head=stack(postfix[0])
bottom=head #used for pop
for i in range(1,len(postfix)):
    head=head.push(postfix[i])


for i in range(0,len(postfix)):
    head=bottom.pop(head)
    
    
 
