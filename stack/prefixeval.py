############################
# Prefix evaluation using stack(singlely linked list)
############################
# need two stacks/try with one only
### + 3 + 4 / 20 4
### python prefixeval.py "+ 3 + 4 / 20 4"
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
    
    def printstack(self):
        temp=self
        while temp:
            print temp.data
            temp=temp.next
    
    def evalprefix(self):
        temp=self
        exp=['+','-','*','/']
        while temp and temp.next and temp.next.next:
            if temp.data in exp and temp.next.data not in exp and temp.next.next.data not in exp:
                #pop all 3 ,evaluate and push to stach again
                
            
        
        
            
            
#####################
# main()
#####################

postfix = sys.argv[1]
postfix=postfix.split()
exp=['+','-','*','/']
head=stack(postfix[0])
bottom=head #used for pop
for i in range(1,len(postfix)):
    head=head.push(postfix[i])

#to simplely pop each element one by one from the stack
#for i in range(0,len(postfix)):
    #head=bottom.pop(head)
     
print
bottom.printstack()

bottom.evalprefix()
print
print "evaluating the Prefux Notation now: " 
print



 
