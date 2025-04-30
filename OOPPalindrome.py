class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def isEmpty(self):
        return self.top is None

    def printStack(self):
        current = self.top
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def main():
    user_input = input("Enter a word to check if it's a palindrome: ").lower()
    
    # Convert the string to an array of characters
    char_array = list(user_input)
    s = Stack() # Create a stack object
    
    for char in char_array: # Push each character onto the stack object
        s.push(char)
    
    for char in char_array:
        if char != s.pop():
            print("The input is not a palindrome.")
            return
    print("The input is a palindrome.")
        
if __name__ == "__main__":
    main()