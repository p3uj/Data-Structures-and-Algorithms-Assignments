class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.curr = None

    def insert_value(self, data):
        node = Node(data)   # Create a node
        if self.head is None:
            self.head = node    # Assign the head to a first node that was created.
        else:
            self.curr.next = node    # Linked the next of the curr node to new node.
        node.next = self.head   # Linked the next of the new node to head node.
        self.curr = node    # Assign curr to the new node.

    def printing(self):
        if self.head is not None:
            print("Circular Linked List: ", end="")
            number_of_nodes = 1
            print(f"{self.head.data}  ", end="")
            self.curr = self.head.next  # Assign curr to the next node of the head node.
            while self.curr != self.head:
                number_of_nodes += 1    # Accumulate all the nodes that will be passed.
                print(f"{self.curr.data}  ", end="")
                self.curr = self.curr.next  # Assign the curr to the next node for preparation to the next loop.
            print(f"\nNumber of Nodes: {number_of_nodes}")
        else:
            print("No record/s in the Circular Linked List!")
            return

created_circ_linked_list = CircularLinkedList()
created_circ_linked_list.insert_value(5)
created_circ_linked_list.insert_value(9)
created_circ_linked_list.insert_value(11)
created_circ_linked_list.insert_value(17)
created_circ_linked_list.insert_value(35)
created_circ_linked_list.insert_value(57)
created_circ_linked_list.insert_value(83)
created_circ_linked_list.printing()