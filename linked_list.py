class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        
    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 0
            while current and count < position - 1:
                current = current.next
                count += 1
            if current:
                new_node.next = current.next
                current.next = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("END")

    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

        print(f"{data} not found in the list.")
            
            
            
linked_list = linkedlist()

linked_list.append(5)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(3)


print("Linked List :")

linked_list.display()
print("")          
print("Adding an elements in the linked list at the beginning!! ")
linked_list.add(51)
linked_list.display()
linked_list.add(17)
linked_list.display()
linked_list.add(38)
linked_list.display()

print("")
print("Adding an elements in the linked list at the ending!! ")
linked_list.append(10)
linked_list.display()
linked_list.append(15)
linked_list.display()
linked_list.append(20)
linked_list.display()

print("")
print("Adding an elements in the linked list at the particular index!! ")

linked_list.insert(3, 0)
linked_list.display()
linked_list.insert(4, 5)
linked_list.display()
linked_list.insert(2, 9)
linked_list.display()

print("")
print("The final linked list after adding an elements:")
linked_list.display()

print("")
print("Deleting an element in linked list!!")

linked_list.delete(51)
linked_list.display()
linked_list.delete(5)
linked_list.display()
linked_list.delete(9)
linked_list.display()
linked_list.delete(63)
linked_list.display()
linked_list.delete(3)
linked_list.display()
print("")
print("The final linked list after deleting an elements:")
linked_list.display()


