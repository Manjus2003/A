from collections import deque

class ImplmentStackUsingTwoQueues:

    def __init__(self):
        self.q1=deque()
        self.q2=deque()


    def push(self,ele):
        self.q2.append(ele)

        while(len(self.q1)!=0):
            self.q2.append(self.q1.pop())
        self.q1,self.q2=self.q2,self.q1


    def pop(self):
        
        if len(self.q2)!=0:
            return self.q2.pop(0)


