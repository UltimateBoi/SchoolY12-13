stack = [None for _ in range(10)] # list comprehension

top=-1

def push(num):
    global top
    if top == len(stack)-1:
        print("Stack is full.")
        return
    top += 1
    stack[top] = num

def pop():
    global top
    if top == -1:
        print("Stack is empty.")
        return
    stack[top] = None
    top -= 1

def isFull():
    global top
    if top == len(stack)-1:
        return True
    return False

def isEmpty():
    global top
    if top == -1:
        return True
    return False

def main():
    myString = input("Please enter a word or phrase to be tested: ").lower()
    for char in myString:
        push(char)

    reversed_str = ""
    while not isEmpty():
        reversed_str += stack[top]
        pop()

    if myString == reversed_str:
        print("The input is a palindrome.")
    else:
        print("The input is not a palindrome.")
    

if __name__ == "__main__":
    main()