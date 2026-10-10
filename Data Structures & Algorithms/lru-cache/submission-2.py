class Node:
    def __init__(self, key:int=0, val:int=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev= None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key: Node
        self.capacity = capacity
        self.size = 0

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    def insertToEnd(self, node: Node):
        prev = self.tail.prev
        prev.next = node
        node.next = self.tail
        node.prev = prev
        self.tail.prev = node
        self.size += 1
        if self.size > self.capacity:
            old = self.head.next
            self.remove(old)
            del self.cache[old.key]
    
    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            res = node.val
            self.remove(node)
            self.insertToEnd(node)
            return res
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
        else:
            self.cache[key] = Node(key, value)
        self.insertToEnd(self.cache[key])
        
