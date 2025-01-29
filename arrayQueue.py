busQueue = [0 for _ in range(5)] # 10 buses using list comprehension
print(busQueue,end="\n\n")

front = 0
rear = -1

currentSize = 0
maxSize = 5

def enqueue(bus):
    global rear, currentSize
    rear += 1 # add item to queue
    busQueue[rear] = bus # add bus to queue
    currentSize += 1 # increment current size

def dequeue():
    global front, currentSize
    bus = busQueue[front] # get bus from queue
    front += 1 # change front pointer to +1
    currentSize -= 1 # decrement current size
    return bus # return bus

def isFull():
    global currentSize
    return currentSize == maxSize # check if queue is full

def isEmpty():
    global front, rear
    # Check if front index is greater than rear index because front is always ahead of rear unless the queue is empty
    return front > rear

print("front rear:", front, rear)
print("Is queue full?", isFull())
print("Is queue empty?", isEmpty(),end="\n\n")

enqueue(1)
enqueue(2)

print((busQueue),end="\n\n")

print("front rear:", front, rear,end="\n\n")
print("Is queue full?", isFull())
print("Is queue empty?", isEmpty(),end="\n\n")

enqueue(3)
enqueue(4)

print(busQueue)
print("front rear:", front, rear,end="\n\n")

# test max size of queue

enqueue(5)

print(busQueue)
print("front rear:", front, rear)
print("Is queue full?", isFull(),end="\n\n")

# test dequeue

print("Dequeue:", dequeue())
print(busQueue)
print("front rear:", front, rear,end="\n\n")

print("Dequeue:", dequeue())
print(busQueue)
print("front rear:", front, rear,end="\n\n")