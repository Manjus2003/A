from SingleLinkedList import SingleLinkedList

s1=SingleLinkedList()
#s1.add_at_head(10)
#s1.add_at_tail(20)
#s1.add_at_tail(30)
#s1.add_at_tail(40)
#s1.add_at_tail(50)


s2=SingleLinkedList()
#s2.add_at_head(60)
#s2.add_at_tail(70)
#s2.add_at_tail(30)
#s2.add_at_tail(50)
#s2.add_at_tail(40)


def mergeUnique(s1,s2):
    
    set1=set()

    first=s1.head

    while first:
        set1.add(first.data)
        first=first.next

    second=s2.head

    while second:
        if second.data not in set1:
            s1.add_at_tail(second.data)
        second=second.next        

    return s1.display()

print(mergeUnique(s1,s2))
