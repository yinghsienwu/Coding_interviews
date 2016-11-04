class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_help(self.root, new_val)
        
    def insert_help(self, current, new_val):
        if new_val > current.value:
            if current.right:
                self.insert_help(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_help(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.search_help(self.root, find_val)

    def search_help(self, current, find_val):
        if current: 
            if current.value == find_val:
                return True
            elif find_val > current.value:
                return self.search_help(current.right, find_val)
            else:
                return self.search_help(current.left, find_val)
        
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
