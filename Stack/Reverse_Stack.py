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


def reverse_file_linewise(sample, reversed_sample):
    with open(sample, "r") as f:
        lines = f.readlines()

    with open(reversed_sample, "w") as f:
        for line in lines:
            stack = Stack()   # ✅ using Stack class now
            for ch in line.strip("\n"):
                stack.push(ch)

            reversed_line = ""
            while not stack.is_empty():
                reversed_line += stack.pop()

            f.write(reversed_line + "\n")


# Example usage
reverse_file_linewise("sample.txt", "reversed_sample.txt")
print("Line-wise reversed text written to reversed_sample.txt")
        