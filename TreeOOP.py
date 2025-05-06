class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self, root_value):
        self.root = Node(root_value)
    
    def add(self, value):
        current = self.root
        while True:
            if value < current.value: # left pointer
                if current.left is None: # if the left pointer is empty (null)
                    current.left = Node(value) # set the left pointer to the new node
                    break # exit the while loop
                else: # if the left pointer is not empty
                    current = current.left # move to the left child
            else:
                if current.right is None:
                    current.right = Node(value)
                    break
                else:
                    current = current.right
    
    def print_tree(self):
        stack = []
        current = self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(current.value, end=" ")
            current = current.right

if __name__ == "__main__":
    tree = Tree(10)
    tree.add(5)
    tree.add(15)
    tree.add(3)
    tree.add(7)
    tree.add(12)
    tree.add(18)
    
    print("In-order traversal of the binary tree:")
    tree.print_tree()
    print("\n")