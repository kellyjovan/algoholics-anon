from queue import SimpleQueue

class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def add(self, val):
        curr = self
        newNode = BST(val)

        while True:
            if val == curr.val:
                return

            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = newNode
                    break
            elif val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = newNode
                    break

    def inorder(self, cb = print):
        if self.left:
            self.left.inorder(cb)
        
        cb(self.val)

        if self.right:
            self.right.inorder(cb)

    def preorder(self, cb = print):
        cb(self.val)

        if self.left:
            self.left.preorder(cb)
        
        if self.right:
            self.right.preorder(cb)

    def postorder(self, cb = print):
        if self.left:
            self.right.postorder(cb)
        
        if self.right:
            self.right.postorder(cb)

        cb(self.val)

    def breath_first(self, cb = print):
        queue = SimpleQueue()
        queue.put(self)

        while not queue.empty():
            first = queue.get()
            cb(first.val)

            if first.left:
                queue.put(first.left)

            if first.right:
                queue.put(first.right)
    
    def height(self):
        left_height = 0 if not self.left else self.left.height()
        right_height = 0 if not self.right else self.right.height()

        return 1 + max(left_height, right_height)

    def min(self):
        if self.left == None:
            print(self.val)
        else:
            self.left.min()

    def max(self):
        if self.right == None:
            print(self.val)
        else:
            self.right.max()

    def contains(self, val):
        if self.val == val:
            return True
        elif val < self.val:
            return False if not self.left else self.left.contains(val)
        elif val > self.val:
            return False if not self.right else self.right.contains(val)

root = BST(10)
root.add(5)
root.add(15)
root.add(3)
root.add(1)
root.add(2)
root.add(18)
root.add(21)

root2 = BST(15)
root2.add(10)
root2.add(20) 

print('--- In Order ---')
root.inorder()
print('--- Pre Order ---')
root.preorder()
print('--- Post Order ----')
root.postorder()
print('--- Breath First ----')
root.breath_first(lambda val: print('hah ahah {}'.format(val)))
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