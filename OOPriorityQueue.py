import os

# Node class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
    
    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next = next

# LinkedList class

class LinkedList:
    def __init__(self):
        # Define the size, maxSize, front, and rear members of the linked list
        self.size = 0
        self.maxSize = 5
        self.front = 0
        self.rear = -1
    
    def enqueue(self, data): # enqueue busses baserd on their priority (e.g. 123A, 153A, 121A, 123B, 153B, 121B) when enqueueing these busses
        if self.isFull():
            print("Queue is full. Cannot enqueue.")
        else:
            newNode = Node(data)
            if self.rear == -1: # queue is empty
                self.front = newNode # front and rear point to the same node
                self.rear = newNode # front and rear point to the same node
            else:
                current = self.front
                previous = None
                # First order the queue based on the bus letter (A, B, C, etc. located at the end of a bus e.g. 123A, 153A, 121A)
                # Then order the queue based on the bus number (e.g. 123, 153, 121)
                while current != None and (current.getData()[-1] < newNode.getData()[-1] or 
                      (current.getData()[-1] == newNode.getData()[-1] and int(current.getData()[:-1]) < int(newNode.getData()[:-1]))):
                    previous = current
                    current = current.getNext()
                if previous == None: # Insert at the front
                    newNode.setNext(self.front) # Set the next of the new node to the front
                    self.front = newNode # Set the front to the new node
                else: # Insert in the middle or at the end if the data of the new node is greater than the data of the current node
                    previous.setNext(newNode) # Set the next of the previous node to the new node
                    newNode.setNext(current) # Set the next of the new node to the current node
                if current == None:
                    self.rear = newNode
            self.size += 1
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty. Cannot dequeue.")
            return None
        else: # Dequeue the bus at the front of the queue
            data = self.front.getData() # Get the data of the front node
            self.front = self.front.getNext() # Set the front to the next node
            self.size -= 1 # Decrement the size of the queue
            return data
        
    def isFull(self):
        return self.size == self.maxSize
    
    def isEmpty(self):
        return self.size == 0
    
    def printQueue(self):
        if self.isEmpty():
            print("Queue is empty.")
        else:
            current = self.front
            while current != None:
                print(current.getData(), end=" ")
                current = current.getNext()
            print()

# Menu system testing

def menu():
    busQueue = LinkedList() # Instantiate a linked list object
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nPlease choose an option:\n")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Print Queue")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            bus = input("Enter bus number: ")
            busQueue.enqueue(bus)
        elif choice == '2':
            bus = busQueue.dequeue()
            if bus != None:
                print(f"Bus {bus} dequeued.")
        elif choice == '3':
            busQueue.printQueue()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
        input("\nPress Enter to continue...")

menu()