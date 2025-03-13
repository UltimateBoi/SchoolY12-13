class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

myString = input("Please enter a word or phrase to be tested: ").lower()


list1 = list(myString)  # convert myString to a list of characters
numChars = len(list1)
s = Stack()  # Assume Stack has push, pop and isEmpty methods

# Push each character onto the stack
for i in range(numChars):
    s.push(list1[i])

# Pop characters from the stack to form the reversed version
reversedList = []
while not s.isEmpty():
    reversedList.append(s.pop())

# Check if the original list is equal to the reversed list
if list1 == reversedList:
    print("The input is a palindrome.")
else:
    print("The input is not a palindrome.")