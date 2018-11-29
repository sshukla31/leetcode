# Link list. Can be used as doubly or singly link list.
# previous is for doubly.



class Node(object):
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next= new_node

        new_node.previous = self.tail
        self.tail = new_node

    def search(self, value):
        temp = self.head
        present = False
        while(temp is not None):
            if temp.data == value:
                print "Present"
                present = True
            temp = temp.next

        if not present:
            print "{} not found".format(value)

    def get_node(self, value):
        temp = self.head
        while(temp is not None):
            if temp.data == value:
                return temp

            temp = temp.next

        return None

    def remove_all(self):
        while(self.head is not None):
            temp = self.head.next
            self.head = None
            self.head = temp

    def delete(self, value):
        temp = self.head
        while(temp is not None):
            if temp.data == value:
                print "Deleting {}".format(value)
                temp.previous.next = temp.next
                if temp.next is not None:
                    temp.next.previous = temp.previous
            temp = temp.next

    def print_result(self):
        temp = self.head
        while(temp is not None):
            print temp.data
            temp = temp.next

    def print_reverse(self):
        temp = self.tail
        while(temp is not None):
            print temp.data
            temp = temp.previous


if __name__ == '__main__':
    link_list = LinkList()
    for val in range(0, 5):
        link_list.add(val)

    link_list.print_result()
    print "Print reverse"
    link_list.print_reverse()

    link_list.search(3)
    link_list.search(10)

    print "Delete value 3"
    link_list.add(3)
    link_list.delete(3)
    link_list.print_result()

    print "Delete all nodes"
    link_list.remove_all()
    link_list.print_result()

