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
        self.size = 0
        self.maxSize = 5
        self.front = 0
        self.rear = -1
    
    def enqueue(self, data): # circular queue using nodes members of a linked list
        if self.isFull():
            print("Queue is full. Cannot enqueue.")
        else:
            newNode = Node(data)
            if self.rear == -1: # queue is empty
                self.front = newNode # front and rear point to the same node
                self.rear = newNode # front and rear point to the same node
            else:
                self.rear.setNext(newNode)
                self.rear = newNode
            self.size += 1
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty. Cannot dequeue.")
            return None
        else:
            data = self.front.getData()
            self.front = self.front.getNext()
            self.size -= 1
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