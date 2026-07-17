class Node:
    def __init__(self,coeff,exp):
        self.coeff=coeff
        self.exp=exp
        self.next=None
class polynomial:
    def __init__(self):
        self.head=None

def insert(self,coeff,exp):
    new_node=Node(coeff,exp)
    if self.head is None:
        self.head=new_node
        return
    current=self.head
    while current:
        if current.exp==exp:
            current.coeff +=coeff
            return
        if current.next is None:
            break
        current=current.next
    current.next=new_node
def delete(self,exp):
    current=self.head
    privious=None
    while current:
        if previous is None:
            self.head=current.next
        else:
            previous.next=current.next

    
    
