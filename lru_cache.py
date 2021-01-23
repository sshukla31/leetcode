# def say_hello():
#     print 'Hello, World'

# for i in xrange(5):
#     say_hello()


#
# Your previous Plain Text content is preserved below:
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

# capacity of 5
# set(1,1) -> 11
# set(2,2) ->  22 11
# set(3,3) -> 33 22 11
# set (1,9) -> 19 33 22
# set (4,4) -> 44 19 33 22
# get (3) -> 3 -> 33 44 19 22
# set(5,5) -> 55 33 44 19 22
# set(6,6) -> 66 55 33 44 19
# get(2) -> -1 -> 66 55 33 44 19
# get(1) -> 9 -> 19 66 55 33 44




class Node(object):
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.cache = dict()
        self.size = 0
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head


    def add_new_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev = node.prev
        new_node = node.next
        prev.next = new_node
        new_node.prev = prev

    def move_head(self, node):
        # 1: Remove node
        self.remove_node(node)

        # 2: Add node
        self.add_new_node(node)



    def set(self, key, value):
        node = self.cache.get(key, None)

        if node:
            node.value = value
            self.move_head(node)
        else:
            temp_node = Node()
            temp_node.key = key
            temp_node.value = value

            self.cache[key] = temp_node
            self.add_new_node(temp_node)

            self.size += 1

            if self.capacity < self.size:
                tail = self.tail.prev
                self.remove_node(tail)

                del self.cache[tail.key]
                self.size -= 1


    def get(self, key):
        node = self.cache.get(key, None)

        if node:
            self.move_head(node)
            return node.value
        else:
            return -1


lru = LRUCache(5)
# capacity of 5
lru.set(1,1)  # -> 11
lru.set(2,2)  #  22 11
lru.set(3,3)  # 33 22 11
lru.set (1,9) # 19 33 22
lru.set (4,4) # 44 19 33 22
print lru.get (3)   #3 -> 33 44 19 22
lru.set(5,5)  # 55 33 44 19 22
lru.set(6,6)  # 66 55 33 44 19
print lru.get(2)     # -> -1 -> 66 55 33 44 19
print lru.get(1) # -> 9 -> 19 66 55 33 44
print lru.get(3)
print lru.set(7, 7)
print lru.get(4)





