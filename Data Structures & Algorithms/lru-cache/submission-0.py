class Node:
    def __init__(self, key=0, val=0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeMap = {} # key -> node
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def update(self, key):
        # update the key to the end of the linkedlist
        curr = self.nodeMap[key]
        prev, nxt = curr.prev, curr.next
        prev.next = nxt
        nxt.prev = prev
        curr_last = self.tail.prev
        curr_last.next = curr
        curr.prev = curr_last
        curr.next = self.tail
        self.tail.prev = curr


    def get(self, key: int) -> int:
        # Return the value corresponding to the key if the key exists, otherwise return -1.
        val = -1
        if key in self.nodeMap:
            val = self.nodeMap[key].val
            self.update(key)
        return val
        
    def remove(self):
        node = self.head.next
        del self.nodeMap[node.key]
        nxt = self.head.next.next
        self.head.next = nxt
        nxt.prev = self.head
        self.size -= 1
    def put(self, key: int, value: int) -> None:
        # update the value of the key if the key exists. 
        if key in self.nodeMap:
            self.nodeMap[key].val = value
            self.update(key)
        # Otherwise, add the key-value pair to the cache. 
        else:
            new_node = Node(key, value)
            prev = self.tail.prev
            prev.next = new_node
            new_node.next = self.tail
            new_node.prev = prev
            self.tail.prev = new_node
            self.size += 1
            self.nodeMap[key] = new_node
        # If the introduction of the new pair causes the cache to exceed its capacity, 
        if self.size > self.capacity:
            self.remove()
        # remove the least recently used key.
        
