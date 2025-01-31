import os

busQueue = [0 for _ in range(5)] # 5 buses using list comprehension

front = 0 # points to the first item in the queue
rear = -1 # points to the last item in the queue (-1 means the queue is empty)

currentSize = 0
maxSize = 5

def enqueue(bus):
    global rear, currentSize
    if isFull():
        print("Queue is full. Cannot enqueue.")
    else:
        rear = (rear + 1) % maxSize # add item to queue and wrap around if needed
        busQueue[rear] = bus # add bus to queue
        currentSize += 1 # increment current size

def dequeue():
    global front, currentSize
    if isEmpty():
        print("Queue is empty. Cannot dequeue.")
        return None
    else:
        bus = busQueue[front] # get bus from queue
        front = (front + 1) % maxSize # wrap around if needed
        currentSize -= 1 # decrement current size
        return bus # return bus

def isFull():
    global currentSize
    return currentSize == maxSize # check if queue is full

def isEmpty():
    global currentSize
    return currentSize == 0 # check if queue is empty

def printQueue():
    global front, rear, currentSize
    if isEmpty():
        print("Queue is empty.")
    else:
        index = front
        for _ in range(currentSize):
            print(busQueue[index], end=" ")
            index = (index + 1) % maxSize
        print()

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nPlease choose an option:\n")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Print Queue")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            bus = int(input("Enter bus number to enqueue: "))
            enqueue(bus)
        elif choice == '2':
            bus = dequeue()
            if bus is not None: # check if bus is dequeued
                print(f"Dequeued bus: {bus}")
        elif choice == '3':
            print("Current Queue: ", end="")
            printQueue()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
        input("Press Enter to continue...")

menu()