class Stack:    
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)
    
    
def is_balanced(exp):
        s=Stack()
        balanced=True
        
        for i in exp:
            if i=='(':
                s.push(i)
            elif i==')':
                if s.is_empty():
                    balanced=False
                    break
                else:
                    s.pop()
        return balanced and s.is_empty()
    
def main():
        exp=input("Enter the expression: ")
        if is_balanced(exp):
            print("The parentheses are balanced.")
        else:
            print("The parentheses are not balanced.")

if __name__ == "__main__":
    main()    
        
                    