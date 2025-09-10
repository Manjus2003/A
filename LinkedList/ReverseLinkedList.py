from SingleLinkedList import SingleLinkedList

s1=SingleLinkedList()
s1.add_at_head(10)
s1.add_at_tail(20)
s1.add_at_tail(30)
s1.add_at_tail(40)
s1.add_at_tail(50)

def reverseLinkedList(s1):
    prev=None
    cur =s1.head
    while cur:
        next_node=cur.next 
        cur.next=prev
        prev=cur
        cur=next_node

    s1.head=prev
    return s1.display()


print(reverseLinkedList(s1))


