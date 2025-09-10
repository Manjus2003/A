from SingleLinkedList import SingleLinkedList

s=SingleLinkedList()
s.add_at_head(10)
s.add_at_tail(20)
s.add_at_tail(30)
s.add_at_data(2,25)
s.add_at_data(10,35)

n=int(input("Enter the number:"))

def sum_of_last_n_numbers(s,n):
    head=s.head

    if not head or n <= 0:
        return 0
    
    first=second=head

    for _ in range(n):
        if not first:
            return "Number is out of range"
        first=first.next
        
    while  first:
        first=first.next
        second =second.next

    total=0    
    while  second:
        total+=second.data
        second=second.next

    return total    


print(sum_of_last_n_numbers(s,n))