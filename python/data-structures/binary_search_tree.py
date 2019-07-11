from queue import SimpleQueue

class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        curr = self
        newNode = BST(key)

        while True:
            if key == curr.key:
                return

            if key < curr.key:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = newNode
                    break
            elif key > curr.key:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = newNode
                    break

    def is_leaf(self):
        return not self.left and not self.right

    def delete(self, key):
        if self.key == key:
            if self.is_leaf():
                return None
            
            if self.left == None:
                return self.right

            if self.right == None:
                return self.left

            smallest = self.right.min()
            self.key = smallest.key
            self.right = self.right.delete(smallest.key)
            return self

        if key < self.key and self.left:
            self.left = self.left.delete(key)
            return self
        
        if key > self.key and self.right:
            self.right = self.right.delete(key) 
            return self

    def inorder(self, cb = print):
        if self.left:
            self.left.inorder(cb)
        
        cb(self.key)

        if self.right:
            self.right.inorder(cb)

    def preorder(self, cb = print):
        cb(self.key)

        if self.left:
            self.left.preorder(cb)
        
        if self.right:
            self.right.preorder(cb)

    def postorder(self, cb = print):
        if self.left:
            self.right.postorder(cb)
        
        if self.right:
            self.right.postorder(cb)

        cb(self.key)

    def breath_first(self, cb = print):
        queue = SimpleQueue()
        queue.put(self)

        while not queue.empty():
            first = queue.get()
            cb(first.key)

            if first.left:
                queue.put(first.left)

            if first.right:
                queue.put(first.right)
    
    def height(self):
        left_height = 0 if not self.left else self.left.height()
        right_height = 0 if not self.right else self.right.height()

        return 1 + max(left_height, right_height)

    def min(self):
        if not self.left:
            return self
        else:
            return self.left.min()

    def max(self):
        if self.right == None:
            return self
        else:
            self.right.max()

    def contains(self, key):
        if self.key == key:
            return True
        elif key < self.key:
            return False if not self.left else self.left.contains(key)
        elif key > self.key:
            return False if not self.right else self.right.contains(key)

root = BST(10)
root.insert(5)
root.insert(15)
root.insert(3)
root.insert(1)
root.insert(2)
root.insert(18)
root.insert(21)

root2 = BST(15)
root2.insert(10)
root2.insert(20) 

print('--- In Order ---')
root.inorder()
print('--- Pre Order ---')
root.preorder()
print('--- Post Order ----')
root.postorder()
print('--- Breath First ----')
root.breath_first(lambda key: print('hah ahah {}'.format(key)))
print('--- Min ---')
root.min()
print('--- Max --- ')
root.max()
print('--- Contains ---')
print(root.contains(18))
print(root.contains(2))
print(root.contains(99))
print('--- Height ----')
print(root.height())
print(root2.height())

root.delete(10)
root.delete(15)
root.delete(18)
root.delete(23)
print('---')
root.inorder()