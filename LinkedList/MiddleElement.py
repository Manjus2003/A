from SingleLinkedList import *

def find_middle(s6):
    fast=slow=s6.head
    
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next


    return slow.data


s6=SingleLinkedList()
s6.add_at_tail(10)
s6.add_at_tail(20)
s6.add_at_tail(30)
s6.add_at_tail(40)
s6.add_at_tail(50)
s6.add_at_tail(60)
s6.add_at_tail(70)
s6.add_at_tail(80)


print(find_middle(s6))