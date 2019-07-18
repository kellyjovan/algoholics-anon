class LLNode:
    def __init__(self, key: int = None, val: int = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        
        self.head = LLNode()
        self.tail = LLNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        self.size += 1
        
        node.next = self.head.next
        self.head.next.prev = node
        
        node.prev = self.head
        self.head.next = node
        
        
        
    def _move_to_front(self, node: LLNode):
        self._remove_node(node)
        self._add_node(node)
        
    def _remove_node(self, node: LLNode):
        self.size -= 1
        
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def _pop_tail(self):
        least_used = self.tail.prev
        
        self._remove_node(least_used)
        
        return least_used
    
    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_front(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.size == self.capacity:
                least_used = self._pop_tail()
                del self.cache[least_used.key]
        
            new_node = LLNode(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
        else:
            node = self.cache[key]
            node.val = value
            self._move_to_front(node)