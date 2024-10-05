
'''
Source: ChatGpt
To understand B-tree, let's first understand the concept of a B-tree. 
A B-tree is a self-balancing tree data structure that maintains sorted data 
and allows searches, sequential access, insertions, and deletions in logarithmic time. 
The B-tree generalizes the binary search tree, 
allowing for nodes with more than two children. 
It is commonly used in databases and file systems.
'''
class BTreeNode:
    def __init__(self, leaf=False):
        # Whether the node is a leaf or not (True = leaf, False = internal node)
        self.leaf = leaf
        # List to store the keys (numbers) in this node
        self.keys = []
        # List to store references to child nodes (used only for internal nodes)
        self.children = []

class BTree:
    def __init__(self, t):
        # Initialize the tree with a minimum degree (t)
        # Each node (except the root) must have at least t-1 keys and can have at most 2t-1 keys.
        self.root = BTreeNode(True)  # Start with an empty root node, which is a leaf
        self.t = t  # Minimum degree that defines the range of number of keys a node can hold

    def search(self, k, node=None):
        # Recursive search function to find a key 'k' in the B-tree
        if node is None:
            node = self.root  # Start searching from the root if node is not provided

        # Find the first key greater than or equal to k
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1

        # If the key is found, return it
        if i < len(node.keys) and k == node.keys[i]:
            return node.keys[i]

        # If the node is a leaf, and we haven't found the key, return None
        if node.leaf:
            return None

        # If not a leaf, recurse to the appropriate child
        return self.search(k, node.children[i])

    def insert(self, k):
        # Insert a key into the B-tree, starting with the root
        root = self.root
        # If the root node is full (has 2t - 1 keys), split it
        if len(root.keys) == (2 * self.t) - 1:
            new_node = BTreeNode(False)  # Create a new root node (will not be a leaf)
            self.root = new_node  # Update root of the tree
            new_node.children.append(root)  # The old root becomes the child of the new root
            self.split_child(new_node, 0)  # Split the old root
            self.insert_non_full(new_node, k)  # Insert the key into the non-full new root
        else:
            self.insert_non_full(root, k)

    def split_child(self, parent, i):
        # Split the i-th child of 'parent' node into two nodes
        t = self.t
        node = parent.children[i]
        new_node = BTreeNode(node.leaf)  # New node will have the same leaf status as the old node

        # Move the middle key of 'node' to the 'parent'
        parent.keys.insert(i, node.keys[t - 1])

        # Insert the new node as the right child of the parent
        parent.children.insert(i + 1, new_node)

        # Split the keys of the node
        new_node.keys = node.keys[t:(2 * t) - 1]
        node.keys = node.keys[0:t - 1]

        # If 'node' is not a leaf, split its children
        if not node.leaf:
            new_node.children = node.children[t:(2 * t)]
            node.children = node.children[0:t]

    def insert_non_full(self, node, k):
        # Insert the key into a non-full node
        if node.leaf:
            # If it's a leaf node, find the correct position and insert the key
            i = len(node.keys) - 1
            node.keys.append(None)  # Append a dummy key to make space for the new key
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]  # Shift keys to the right to make space
                i -= 1
            node.keys[i + 1] = k  # Insert the new key in the correct position
        else:
            # If it's not a leaf, find the correct child to recurse into
            i = len(node.keys) - 1
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            # If the child is full, split it before continuing
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], k)


# Dry run with example values

# Create a B-tree with a minimum degree of 2
b_tree = BTree(t=2)

# Inserting values
numbers = [10, 20, 5, 6, 12, 30, 7, 17]

for number in numbers:
    b_tree.insert(number)
    # After each insert, the B-tree reorganizes itself

# Searching for values
print("Search for 17:", b_tree.search(17))  # Found
print("Search for 15:", b_tree.search(15))  # Not Found
