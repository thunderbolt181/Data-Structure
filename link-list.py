class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return self.data

class link_list:
    def __init__(self):
        self.head = None

    def add_node(self,data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
            self.head.prev = self.head
        else:
            node = self.head
            while node.next is not self.head:
                node = node.next
            else:
                n=Node(data)
                n.next=self.head
                n.prev = node
                node.next=n
                self.head.prev=n
        print(self.__repr__())

    def del_node(self):
        if self.head is None:
            print("link list is empty")
        else:
            if self.head.next is self.head:
                self.head = None       
            else:
                node = self.head
                while node.next is not self.head:
                    node = node.next
                else:
                    p_node = node.prev
                    p_node.next=self.head
                    self.head.prev = p_node
                    del(node)
        print(self.__repr__())
    
    def __repr__(self):
        if self.head is not None:
            node=self.head
            while node.next is not self.head:
                print(node.data," -> ",end="")
                node = node.next
            else:
                print(node.data," -> ",end="")
            return "End"

l_list = link_list()
a=1
while(a):
    a = int(input("Enter your choice\n0. Print the Link List and exit\n1. Add a new Node\n2. Delete a node=> "))
    if a==2:
        l_list.del_node()
    elif a==1:
        l_list.add_node(input("Enter Data of new Node => "))
    else:
        pass
print(l_list)