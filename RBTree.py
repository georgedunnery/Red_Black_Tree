# George Dunnery - CS 5800
from BSTNode import *
import math

# Global variable used for visual function
COUNT = [10]


# Class to represent a Red-Black Tree
# Self balancing implementation of a binary search tree
class RBTree:

    # Construct an RBTree object, always starts empty
    def __init__(self):
        self.root = None
        self.sentinel = BSTNode(None, None, None, None, "black")
        self.num_nodes = 0

    # Driver function to allow the user to interact with the RBTree
    def interactive(self) -> None:
        print("--- Interactive Red-Black Tree ---")
        commands = {"quit": "Quit interactive mode.",
                    "exit": "Alternate command to quit interactive mode.",
                    "help": "List out the supported commands.",
                    "print": "Print the keys and colors in order.",
                    "sort": "Print the keys in order.",
                    "exist x": "Check if a node exists in the tree.",
                    "search x": "Prints the information for a node (if exists).",
                    "min": "Print the minimum key.",
                    "max": "Print the maximum key.",
                    "insert x": "Insert a new node with key value = x.",
                    "delete x": "Delete the first instance of node value = x.",
                    "root": "Print the root of the tree."}
        while True:
            # Get the user's input
            user_in = str(input("Please enter a command:\n"))
            # Parse by spaces:
            request = user_in.split(' ')
            # QUIT / EXIT - Exit interactive mode
            if request[0] == "exit" or request[0] == "quit":
                break
            # HELP - Print a list of commands
            elif request[0] == "help":
                print("\t\tHelp Menu")
                for command, desc in commands.items():
                    print(command + " : " + desc)
            # PRINT - Print the current tree keys and colors, in order
            elif request[0] == "print":
                if self.root is not None:
                    print(self.rb_inorder_walk())
                else:
                    print("Tree is empty!")
            # SORT - Output the keys in sorted order (simple inorder walk)
            elif request[0] == "sort":
                if self.root is not None:
                    print(self.sort())
                else:
                    print("Tree is empty!")
            # EXIST - Check if a key exists in the tree
            elif request[0] == "exist":
                try:
                    print(self.in_tree(int(request[1])))
                except IndexError:
                    print("Exist requires an integer parameter: insert x")
                except ValueError:
                    print("Exist requires an integer key!")
            # SEARCH - Search for a node
            elif request[0] == "search":
                try:
                    print(self.search(int(request[1])))
                except IndexError:
                    print("Search requires an integer parameter: insert x")
                except ValueError:
                    print("Search requires an integer key!")
            # MIN - Print the minimum value in the tree
            elif request[0] == "min":
                if self.root is not None:
                    print(self.root.min_node())
                else:
                    print("Tree is empty!")
            # MAX - Print the minimum value in the tree
            elif request[0] == "max":
                if self.root is not None:
                    print(self.root.max_node())
                else:
                    print("Tree is empty!")
            # INSERT - Insert a new node into the tree
            elif request[0] == "insert":
                try:
                    self.insert(int(request[1]))
                    print("Success: insert ", request[1])
                except IndexError:
                    print("Insert requires an integer parameter: insert x")
                except ValueError:
                    print("Insert requires an integer key!")
            # DELETE - delete node x from the tree
            elif request[0] == "delete":
                try:
                    self.rb_delete(int(request[1]))
                    print("Success: delete ", request[1])
                except IndexError:
                    print("Delete requires an integer parameter: insert x")
                except ValueError:
                    print("Delete requires an integer key!")
            # VISUAL - print a 2d visualization of the tree
            elif request[0] == "visual":
                if self.root is None:
                    print("Tree is empty!")
                else:
                    self.visual()
            elif request[0] == "root":
                print(self.root)
            # INVALID - Unknown command, take no action
            else:
                print("Unknown command, enter 'help' for a list of commands.")
            # Printed after every request
            print("Tree Height = " + str(self.tree_height()))
            print("-----------------")

    # Function to calculate the height of the tree
    # Can use math to find height in constant time (rb-tree balance guarantee)
    def tree_height(self) -> int:
        height = 0
        try:
            height = math.log(self.num_nodes, 2)
        except ValueError:
            pass
        return math.floor(height)

    # Function to generate string of nodes in order (small to big)
    # Returns string of the in order walk
    def rb_inorder_walk(self) -> str:
        if self.root is None:
            return ""
        node = self.root
        cat = ""
        cat += self.rb_inorder_walk_aux(node, cat)
        # Remove trailing comma and space ', ' with a slice
        return cat[:-2]

    # Auxiliary function to inorder_walk, please use inorder_walk instead
    #  node: BSTNode, the current node
    #  cat: string, concatenating the node data in the right order
    # Returns a string of the in order walk
    def rb_inorder_walk_aux(self, node: 'BSTNode', cat: str) -> str:
        if node != self.sentinel:
            cat = self.rb_inorder_walk_aux(node.left, cat)
            cat += '(' + str(node.data) + ': ' + str(node.color) + ')' + ', '
            return self.rb_inorder_walk_aux(node.right, cat)
        else:
            return cat

    # Function to return a list of the keys in sorted order
    # Returns a list of integers, the keys in sorted order
    def sort(self) -> list:
        if self.root is None:
            return []
        else:
            walk = self.root.inorder_walk()
            sorted_list = list(map(int, walk.strip().split(',')))
            return sorted_list

    # Function to check if a node exists in the tree
    #  key: integer, the value of the node to search for
    # Returns bool, true if the node exists, otherwise false
    def in_tree(self, key: int) -> bool:
        if self.root is not None:
            return self.root.exist_node(key)
        return False

    # Function to find a particular node in the tree
    # Important: duplicates are allowed, search finds the first instance
    #  key: integer, the value of the node to look for
    # Returns the first instance of a node with this key, or None if not found
    def search(self, key: int) -> 'BSTNode' or None:
        if self.root is not None:
            return self.root.search_node(key)
        return None

    # Function to return the minimum value in the tree
    # Returns integer, the min value or None if the tree is empty
    def min(self) -> 'BSTNode' or None:
        if self.root is not None:
            return self.root.min_node()
        return None

    # Function to return the maximum value in the tree
    # Returns integer, the max value or None if the tree is empty
    def max(self) -> 'BSTNode' or None:
        if self.root is not None:
            return self.root.max_node()
        return None

    # Function to insert a new node into the RBTree
    # Fixes the tree to maintain the red-black property
    #  key: integer, the value of the node to add to the tree
    def insert(self, key: int) -> None:
        self.num_nodes += 1
        parent = self.sentinel
        node = self.root
        while node != self.sentinel:
            # Initial Case, root is None, parent = self.sentinel
            if node is None:
                break
            parent = node
            if key > node.data:
                node = node.right
            else:
                node = node.left
        new_node = BSTNode(key, parent, self.sentinel, self.sentinel, "red")
        # Initial Case: When tree is empty - assign root and sentinel
        if parent == self.sentinel:
            self.root = new_node
        # Usual Case: Place insert the new node by comparisons
        elif new_node.data > parent.data:
            parent.right = new_node
        else:
            parent.left = new_node
        # Left & Right already = sentinel, color already red
        # Red-Black Tree property may be violated, call maintenance
        self.insert_maintenance(new_node)

    # Function to repair the red-black property after an insert is made
    # From CLRS 3rd Ed. p 316, modified (z = node, y = uncle)
    #  node: BSTNode, the node that was just added to the tree
    # Returns nothing
    def insert_maintenance(self, node: 'BSTNode') -> None:
        while node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                # Case 1-L
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    # Case 2-L
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    # Case 3-L
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            else:
                # "if node.parent == node.parent.parent.right"
                uncle = node.parent.parent.left
                # Case 1-R
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    # Case 2-R
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    # Case 3-R
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)
        # Finally, ensure that the root is black to adhere to RBTree rules
        self.root.color = "black"

    # Function to perform left rotate on subtree rooted at node
    # Warning: This function mutates structure of the RBTree!
    #  node: BSTNode, the root of the subtree to left rotate
    # Returns nothing, but mutates the tree during maintenance
    def left_rotate(self, node: 'BSTNode') -> None:
        # Set the node to migrate
        swap = node.right
        # Point node's right subtree to swap's left subtree
        node.right = swap.left
        if swap.left != self.sentinel:
            swap.left.parent = node
        # Set node's parent as swap's parent
        swap.parent = node.parent
        if node.parent == self.sentinel:
            self.root = swap
        elif node == node.parent.left:
            node.parent.left = swap
        else:
            node.parent.right = swap
        swap.left = node
        node.parent = swap

    # Function to perform right rotate on subtree rooted at node
    # Warning: This function mutates structure of the RBTree!
    #  node: BSTNode, the root of the subtree to right rotate
    # Returns nothing, but mutates the tree during maintenance
    def right_rotate(self, node: 'BSTNode') -> None:
        swap = node.left
        node.left = swap.right
        if swap.right != self.sentinel:
            swap.right.parent = node
        swap.parent = node.parent
        if node.parent == self.sentinel:
            self.root = swap
        elif node == node.parent.right:
            node.parent.right = swap
        else:
            node.parent.left = swap
        swap.right = node
        node.parent = swap

    # Function to add an array of integers to a linked list
    #  array: list of integers, the keys to add to the RBTree
    # Returns nothing
    def insert_list(self, array: list) -> None:
        for key in array:
            self.insert(key)

    # Function to print a visualization of the tree
    # (left to right instead of top to bottom)
    # Citation: https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/
    # Returns nothing
    def visual(self) -> None:
        if self.root is not None:
            self.visual_aux(self.root, 0)

    # Auxiliary function to visual, please use visual instead
    # Citation: https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/
    #  node: BSTNode, the current node in the tree
    #  space: int, the number that determines the spacing when printing
    def visual_aux(self, node: 'BSTNode', space: int):
        if node.data is None:
            return
        space += COUNT[0]
        self.visual_aux(node.right, space)
        print()
        for i in range(COUNT[0], space):
            print(end=' ')
        print(node)
        self.visual_aux(node.left, space)

    # Function to delete a node from the tree
    # Important: only deletes the first instance of this key
    #  key: integer, the value of the node to delete
    # Returns nothing
    def rb_delete(self, key: int) -> None:
        # Find the node to delete
        old = self.search(key)
        # If the node doesn't exist, take no action
        if old is None:
            return
        # Otherwise, delete the node
        self.num_nodes -= 1
        self.rb_delete_aux(old)

    # Auxiliary function to rb_delete, please use rb_delete instead
    #  old: BSTNode, the node object to delete
    # Returns nothing
    def rb_delete_aux(self, old: 'BSTNode') -> None:
        # x and y to track moving nodes
        # Will be required for maintenance and transplant calls
        y = old
        y_init_color = y.color
        if old.left == self.sentinel:
            x = old.right
            self.rb_transplant(old, old.right)
        elif old.right == self.sentinel:
            x = old.left
            self.rb_transplant(old, old.left)
        else:
            y = old.right.min_node()
            y_init_color = y.color
            x = y.right
            if y.parent == old:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = old.right
                y.right.parent = y
            self.rb_transplant(old, y)
            y.left = old.left
            y.left.parent = y
            y.color = old.color
        if y_init_color == "black":
            self.rb_delete_maintenance(x)

    # Function to transplant a subtree during deletion
    # Warning: this function mutates the tree!
    #  old: BSTNode, the root of the subtree to be replaced
    #  new: BSTNode, the root of the replacement subtree
    # Replaces the subtree rooted at old with that at new
    def rb_transplant(self, old: 'BSTNode', new: 'BSTNode') -> None:
        if old.parent == self.sentinel:
            self.root = new
        elif old == old.parent.left:
            old.parent.left = new
        else:
            old.parent.right = new
        new.parent = old.parent

    # Function to perform maintenance on the RBTree after a deletion
    #  node: BSTNode, the node to start the maintenance from
    # Returns nothing
    def rb_delete_maintenance(self, node: 'BSTNode') -> None:
        while node != self.root and node.color == "black":
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == "red":
                    sibling.color = "black"
                    node.parent.color = "red"
                    self.left_rotate(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == "black" and sibling.right.color == "black":
                    sibling.color = "red"
                    node = node.parent
                else:
                    if sibling.right.color == "black":
                        sibling.left.color = "black"
                        sibling.color = "red"
                        self.right_rotate(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    sibling.right.color = "black"
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                # if node == node.parent.right:
                sibling = node.parent.left
                if sibling.color == "red":
                    sibling.color = "black"
                    node.parent.color = "red"
                    self.right_rotate(node.parent)
                    sibling = node.parent.left
                if sibling.right.color == "black" and sibling.left.color == "black":
                    sibling.color = "red"
                    node = node.parent
                else:
                    if sibling.left.color == "black":
                        sibling.right.color = "black"
                        sibling.color = "red"
                        self.left_rotate(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    sibling.left.color = "black"
                    self.right_rotate(node.parent)
                    node = self.root
            node.color = "black"
