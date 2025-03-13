# Linked list in a physical order but an alphabetically sorted logical order

names = ["Altaf", "Mariam", "Eesa", "Hussain", "Sam", "David", "Kaya", "Rezwan"]

# Create a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None: # If the linked list is empty, set the head to the new node
            self.head = new_node
            return
        last_node = self.head
        while last_node.next: # Traverse the linked list to the last node
            last_node = last_node.next
        last_node.next = new_node

    def remove(self, data):
        current_node = self.head
        if current_node and current_node.data == data: # If the head node is the one to be removed, set the head to the next node (the second node)
            self.head = current_node.next
            current_node = None
            return
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        previous_node.next = current_node.next
        current_node = None

    def traverse(self):
        current_node = self.head
        values = []
        while current_node:
            values.append(current_node.data)
            current_node = current_node.next
        print(", ".join(values))

    def logical_sort(self):
        current_node = self.head
        while current_node:
            next_node = current_node.next
            while next_node:
                if current_node.data > next_node.data:
                    current_node.data, next_node.data = next_node.data, current_node.data
                next_node = next_node.next
            current_node = current_node.next
        return self

linked_list = LinkedList()

for name in names:
    linked_list.add(name)

# Baseline physical order
print("Physical order:")
linked_list.traverse()

# Print physical and logical linked lists
print("\nLogical order:")
sorted_linked_list = linked_list.logical_sort()
sorted_linked_list.traverse()

# Remove a name from the linked list
print("\nRemove David:")
sorted_linked_list.remove("David")
sorted_linked_list.traverse()

print("\nRemove David + Logical order")
sorted_linked_list.remove("David")
sorted_linked_list.traverse()