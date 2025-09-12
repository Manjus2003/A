class Browser:

    def __init__(self):
        self.frontStack=[]
        self.backStack=[]
        
    def visited(self,url):
        self.frontStack.append(url)

    def back(self):
        if len(self.frontStack)==1:
            print("there is no url present")
        else:
            temp=self.frontStack.pop()
            self.backStack.append(temp)
            print(self.frontStack[len(self.frontStack)-1])


    def front(self):
        if len(self.backStack)==1:
            print("there is no url present")
        else:
            temp=self.backStack.pop()
            self.frontStack.append(temp)
            print(self.frontStack[len(self.frontStack)-1])



b=Browser()

b.visited("google.com")
b.visited("youtube.com")
b.visited("flipkart.com")
b.visited("amazon.com")


b.back()
b.back()
b.back()
b.back()
b.front()
b.front()
b.front()

