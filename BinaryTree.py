tree = [
    [ 1 ,"M", 2 ],
    [ 3 ,"H", 4 ],
    [ 5 ,"T", 6 ],
    [ -1 ,"D", -1 ],
    [-1 ,"K", -1 ],
    [-1,"R", -1 ],
    [ -1 ,"X", -1]
]

root = 0
left = 0
right = 2
data = 1

def traverseInOrder(p):
    if tree[p][left] != -1:
        traverseInOrder(tree[p][left])
    print(tree[p][data])
    if tree[p][right] != -1:
        traverseInOrder(tree[p][right])
        
traverseInOrder(root)