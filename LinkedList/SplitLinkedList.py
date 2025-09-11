from SingleLinkedList import *

def split_list(s4):
    l1=SingleLinkedList()
    l2=SingleLinkedList()
    
    first=s4.head
    k=0
    while first:
        if k%2==0:
            l1.add_at_tail(first.data)
        else:
            l2.add_at_tail(first.data)    
        k+=1    
        first=first.next
    return l1.display(),l2.display()


s4=SingleLinkedList()
s4.add_at_tail(10)
s4.add_at_tail(20)
s4.add_at_tail(30)
s4.add_at_tail(40)
s4.add_at_tail(50)
s4.add_at_tail(60)
s4.add_at_tail(70)
s4.add_at_tail(80)
s4.add_at_tail(90)


split_list(s4)