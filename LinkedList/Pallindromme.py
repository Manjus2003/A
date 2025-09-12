from SingleLinkedList import *

from Stack import Stack


def pallindromme(s7):
    first=second=s7.head
    stk=Stack()
    while first:
        stk.push(first.data)
        first=first.next

    while second:
        if second.data!=stk.peek():
            return False
        stk.pop()
        second=second.next
        

    return True    



s7=SingleLinkedList()
s7.add_at_tail(10)
s7.add_at_tail(20)
s7.add_at_tail(30)
s7.add_at_tail(50)
s7.add_at_tail(50)
s7.add_at_tail(20)
s7.add_at_tail(10)

print(pallindromme(s7))


