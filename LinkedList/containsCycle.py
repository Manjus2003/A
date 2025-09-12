from SingleLinkedList import *

def find_cycle(s8):
    fast=slow=s8.head
    
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

        if slow==fast:
            return True

    return False


s8=SingleLinkedList()
s8.add_at_tail(10)
s8.add_at_tail(20)
s8.add_at_tail(30)
s8.add_at_tail(40)
s8.add_at_tail(50)
s8.add_at_tail(60)
s8.add_at_tail(70)
s8.add_at_tail(80)


print(find_cycle(s8))