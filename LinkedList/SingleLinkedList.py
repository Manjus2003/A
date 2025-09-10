class SingleLinkedList:

    class _node_:

        def __init__(self,ele):
            self.data=ele
            self.next=None

    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def is_empty(self):
        return self.count==0
    
    def get_count(self):
        return self.count
    
    def add_at_head(self,ele):
        new_node=self._node_(ele)

        if not self.is_empty():
            new_node.next=self.head
            self.head=new_node
        else:
            self.tail=self.head=new_node

        self.count+=1

    def add_at_tail(self,ele):
        new_node=self._node_(ele)

        if not self.is_empty():
            self.tail.next=new_node
            self.tail=new_node
        else:
            self.tail=self.head=new_node
        self.count+=1

    def add_at_data(self,pos,ele):
        new_node=self._node_(ele)
        if not self.is_empty():
            if pos<=self.count:
                k=0
                cur=self.head
                while cur is not None and k<pos-1:
                    cur=cur.next
                    k+=1

                new_node.next=cur.next
                cur.next=new_node
            else:
                if pos>self.count:
                    self.tail.next=new_node
                    self.tail=new_node

        else:
            self.head=self.tail=new_node

        self.count+=1    

    def display(self):
        if not self.is_empty():
            cur=self.head
            while cur is not None:
                print(cur.data)
                cur=cur.next
        else:
            print("List is empty")        

            

s=SingleLinkedList()
#s.add_at_head(10)
#s.add_at_tail(20)
#s.add_at_tail(30)
#s.add_at_data(2,25)
#s.add_at_data(10,35)
#s.display()