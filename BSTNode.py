# George Dunnery - CS 5800


# Class to represent a node in a red-black binary search tree
class BSTNode:

    # Constructs a BSTNode object
    #  data: integer, the value to store at this node (None when sentinel)
    #  parent: BSTNode, the parent node
    #  left: BSTNode, the left child (default None)
    #  right: BSTNode, the right child (default, None)
    #  color: Color enum, RED or BLACK, the color of the node in the tree
    def __init__(self, data: int or None, parent=None, left=None, right=None, color=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color

    # Defines the string representation of the node
    def __str__(self):
        left = self.left.data
        if left is None:
            left = "sentinel"
        right = self.right.data
        if right is None:
            right = "sentinel"
        parent = self.parent.data
        if parent is None:
            parent = "sentinel"
        return '(' + str(self.data) + ': ' + str(self.color) + ' P=' + str(parent) + ' L=' + str(left) + ' R=' + str(right) + ')'

    # Function to generate string of nodes in order (small to big)
    # Returns string of the in order walk
    def inorder_walk(self) -> str:
        node = self
        cat = ""
        cat += self.inorder_walk_aux(node, cat)
        # Remove trailing comma and space ', ' with a slice
        return cat[:-2]

    # Auxiliary function to inorder_walk, please use inorder_walk instead
    #  node: BSTNode, the current node
    #  cat: string, concatenating the node data in the right order
    # Returns a string of the in order walk
    def inorder_walk_aux(self, node: 'BSTNode', cat: str) -> str:
        # Using only BSTNode, reach default bottom None
        if node is not None:
            cat = self.inorder_walk_aux(node.left, cat)
            # Using RBTree, encounter sentinel
            if node.data is not None:
                cat += str(node.data) + ', '
            return self.inorder_walk_aux(node.right, cat)
        else:
            return cat

    # Function to insert a value into the tree
    # Note: this function is for simple BST, not the RBTree
    # Ex. call root.insert_node(5)
    #  data: integer, the new value to add to the tree
    # Returns nothing
    def insert_node(self, data: int) -> None:
        node = self
        self.insert_node_aux(node, data)

    # Auxiliary function to insert_node, please use insert_node instead
    #  node: BSTNode, the current node in the tree
    #  data: integer, the value of the new node to add to the tree
    # Returns nothing
    def insert_node_aux(self, node: 'BSTNode', data: int) -> None:
        # Go right if data > node.data, go left if data <= node.data (otherwise)
        # If the child is None then insert, otherwise recursive call left or right
        if data > node.data:
            if node.right is None:
                # Create node as right child (assign node.right & new.parent)
                new_node = BSTNode(data, node, None, None, "red")
                node.right = new_node
            else:
                self.insert_node_aux(node.right, data)
        else:
            if node.left is None:
                # Create node as left child (assign node.left & new.parent)
                new_node = BSTNode(data, node, None, None, "red")
                node.left = new_node
            else:
                self.insert_node_aux(node.left, data)

    # Function to find the minimum value node in the tree
    # Returns the node with min value of the tree nodes
    def min_node(self) -> 'BSTNode':
        node = self
        return self.min_node_aux(node)

    # Auxiliary function to min_node, please use min_node instead
    # Method: go left until None
    #  node: BSTNode, the current node
    # Returns the node with minimum value in the tree
    def min_node_aux(self, node: 'BSTNode') -> 'BSTNode':
        # Using only BSTNode, encounter default bottom None
        if node.left is None:
            return node
        # Using RBTree, encounter sentinel
        elif node.left.data is None:
            return node
        else:
            return self.min_node_aux(node.left)

    # Function to find the maximum value node in the tree
    # Returns the node wit max value of the tree nodes
    def max_node(self) -> 'BSTNode':
        node = self
        return self.max_node_aux(node)

    # Auxiliary function to max_node, please use max_node instead
    # Method: go right until None
    #  node: BSTNode, the current node
    # Returns the node with max value of the tree nodes
    def max_node_aux(self, node: 'BSTNode') -> 'BSTNode':
        # Using only BSTNode, encounter default bottom None
        if node.right is None:
            return node
        # Using RBTree, encounter sentinel
        elif node.right.data is None:
            return node
        else:
            return self.max_node_aux(node.right)

    # Function to find the successor of the calling node
    # E.g. min_node > current node
    # Returns the successor node or None when it doesn't exist
    def successor_node(self) -> 'BSTNode' or None:
        node = self
        # Case 1: Minimum in right subtree
        if node.right is not None:
            return node.right.min_node()
        # Case 2: If it exists, lowest ancestor of node w/ left child also ancestor
        # CLRS 3rd ed. pg 292, modified for python 3.6
        ancestor = node.parent
        while ancestor is not None:
            if node.data != ancestor.right.data:
                break
            node = ancestor
            ancestor = ancestor.parent
        return ancestor

    # Function to find the predecessor of the calling node
    # E.g. max_node < current node
    # Returns the predecessor node or None when it doesn't exist
    def predecessor_node(self) -> 'BSTNode' or None:
        node = self
        # Case 1: Maximum in left subtree
        if node.left is not None:
            return node.left.max_node()
        # Case 2: if it exists, lowest ancestor of node w/ right child also ancestor
        ancestor = node.parent
        while ancestor is not None:
            # Similar to case 2 for successor, just change .right to .left
            if node.data != ancestor.left.data:
                break
            node = ancestor
            ancestor = ancestor.parent
        return ancestor

    # Function to query if a node exists in the tree
    #  key: integer, the value of the node to search for
    # Returns bool, true if it exists, otherwise false
    def exist_node(self, key: int) -> bool:
        node = self
        return self.exist_node_aux(node, key)

    # Auxiliary function to search_node, please use search_node instead
    #  node: BSTNode, the current node in the tree
    #  key: integer, the value of the node being searched for
    # Returns bool, true if it exists, otherwise false
    def exist_node_aux(self, node: 'BSTNode', key: int) -> bool:
        # Using only BSTNode, encounter default bottom None
        if node is None:
            return False
        # Using RBTree, encounter sentinel
        elif node.data is None:
            return False
        elif key == node.data:
            return True
        elif key > node.data:
            return self.exist_node_aux(node.right, key)
        else:
            return self.exist_node_aux(node.left, key)

    # Function to find the node with a given key
    #  key: integer, the key of the node to search for
    # Returns the first node found with this key, or None if not found
    def search_node(self, key: int) -> 'BSTNode':
        node = self
        return self.search_node_aux(node, key)

    # Auxiliary function to search_node, please use search_node instead
    #  node: BSTNode, the current node in the tree
    #  key: integer, the node value to search for
    # Returns the first node found with this key, or None if not found
    def search_node_aux(self, node: 'BSTNode', key: int) -> 'BSTNode' or None:
        # Using only BSTNode, encounter default bottom None
        if node is None:
            return None
        # Using RBTree, encounter sentinel
        elif node.data is None:
            return None
        elif key == node.data:
            return node
        elif key > node.data:
            return self.search_node_aux(node.right, key)
        else:
            return self.search_node_aux(node.left, key)
