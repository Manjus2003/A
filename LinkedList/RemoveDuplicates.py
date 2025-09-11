from SingleLinkedList import *

def removeDuplicates(s5):
    set1=set()

    first=s5.head
    temp=None
    while first:
        if first.data not in set1:
            set1.add(first.data)
            temp=first
        else:
            temp.next=first.next 
        first=first.next
    return s5.display()


s5=SingleLinkedList()
s5.add_at_tail(10)
s5.add_at_tail(20)
s5.add_at_tail(30)
s5.add_at_tail(40)
s5.add_at_tail(30)
s5.add_at_tail(40)
s5.add_at_tail(50)
s5.add_at_tail(60)
s5.add_at_tail(70)
s5.add_at_tail(80)
s5.add_at_tail(90)

removeDuplicates(s5)
        

