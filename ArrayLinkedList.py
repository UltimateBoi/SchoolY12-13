import typing

names = ["Jeff", "Jane", "Eduard", "David", "John", None]

print(", ".join([name for name in names if name is not None]))
print("\n\n")
data = 0
pointer = 1
first = 3
nextFree = 5

linkedList = [
    ["Jeff", 1],
    ["Jane", None],
    ["Eduard", 0],
    ["David", 4],
    ["John", 2],
    [None, None]
]

current = first

def traverse():
    try:
        while pointer is not None:
            print(linkedList[current][data])
            current = linkedList[current][pointer]
    except:
        pass
    
    