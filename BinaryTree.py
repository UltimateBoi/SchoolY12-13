treeArray = [
    [ 1 ,"M", 2 ],
    [ 3 ,"H", 4 ],
    [ 5 ,"T", 6 ],
    [ -1 ,"D", -1 ],
    [-1 ,"K", -1 ],
    [-1,"R", -1 ],
    [ -1 ,"X", -1]
]

root = 0
left = 1
right = 2
data = 1

print(treeArray[root][left])

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

print(hex(id(treeArray)))