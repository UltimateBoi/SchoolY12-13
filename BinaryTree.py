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
    print(tree[p][data], end=" ")
    if tree[p][right] != -1:
        traverseInOrder(tree[p][right])

print("Traversal in order: ")
traverseInOrder(root)

def traversePreOrder(p):
    print(tree[p][data],end=" ")
    if tree[p][left] != -1:
        traversePreOrder(tree[p][left])
    if tree[p][right] != -1:
        traversePreOrder(tree[p][right])

print("\nTraversal pre order: ")
traversePreOrder(root)

def traversePostOrder(p):
    if tree[p][left] != -1:
        traversePostOrder(tree[p][left])
    if tree[p][right] != -1:
        traversePostOrder(tree[p][right])
    print(tree[p][data],end=" ")

print("\nTraversal post order: ")
traversePostOrder(root)

def traverseLevelOrder():
    queue = []
    queue.append(root)
    while len(queue) > 0:
        p = queue.pop(0)
        print(tree[p][data], end=" ")
        if tree[p][left] != -1:
            queue.append(tree[p][left])
        if tree[p][right] != -1:
            queue.append(tree[p][right])

print("\nTraversal level order: ")
traverseLevelOrder()
print("\n")