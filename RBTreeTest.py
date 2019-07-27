# George Dunnery - CS 5800
import unittest
from RBTree import *


# Test class focused on BSTNode functionality
class BSTNodeTest(unittest.TestCase):
    # Verify that the node is created correctly
    def test_create_node(self):
        root = BSTNode(10)
        self.assertEqual(10, root.data)
        left = BSTNode(5)
        right = BSTNode(15)
        left.parent = root
        right.parent = root
        root.left = left
        root.right = right
        self.assertEqual(5, root.left.data)
        self.assertEqual(15, root.right.data)
        self.assertEqual(10, left.parent.data)
        self.assertEqual(10, right.parent.data)

    # Verify that the nodes are inserted correctly left
    def test_insert_node_left(self):
        root = BSTNode(10)
        root.insert_node(10)
        self.assertEqual(10, root.left.data)
        root.insert_node(9)
        self.assertEqual(9, root.left.left.data)

    # Verify that the nodes are inserted correctly left
    def test_insert_node_right(self):
        root = BSTNode(10)
        root.insert_node(11)
        self.assertEqual(11, root.right.data)
        root.insert_node(12)
        self.assertEqual(12, root.right.right.data)

    # Verify that left and right children are inserted correctly
    def test_insert_node_full(self):
        root = BSTNode(10)
        root.insert_node(5)
        root.insert_node(7)
        root.insert_node(3)
        root.insert_node(15)
        root.insert_node(12)
        root.insert_node(17)
        # Children
        self.assertEqual(10, root.data)
        self.assertEqual(5, root.left.data)
        self.assertEqual(3, root.left.left.data)
        self.assertEqual(7, root.left.right.data)
        self.assertEqual(15, root.right.data)
        self.assertEqual(12, root.right.left.data)
        self.assertEqual(17, root.right.right.data)
        # Parents
        self.assertEqual(10, root.left.parent.data)
        self.assertEqual(10, root.right.parent.data)
        self.assertEqual(5, root.left.left.parent.data)
        self.assertEqual(5, root.left.right.parent.data)
        self.assertEqual(15, root.right.left.parent.data)
        self.assertEqual(15, root.right.right.parent.data)

    # Verify that the in order walk has the correct order
    def test_inorder_walk_node(self):
        root = BSTNode(10)
        root.insert_node(5)
        root.insert_node(7)
        root.insert_node(3)
        root.insert_node(15)
        root.insert_node(12)
        root.insert_node(17)
        expected_out = "3, 5, 7, 10, 12, 15, 17"
        self.assertEqual(expected_out, root.inorder_walk())

    # Verify that the min value is found
    def test_min_node(self):
        root_a = BSTNode(10)
        root_a.insert_node(5)
        root_a.insert_node(7)
        root_a.insert_node(3)
        root_a.insert_node(15)
        root_a.insert_node(12)
        root_a.insert_node(17)
        self.assertEqual(3, root_a.min_node().data)
        root_b = BSTNode(10)
        root_b.insert_node(15)
        root_b.insert_node(12)
        root_b.insert_node(17)
        self.assertEqual(10, root_b.min_node().data)

    # Verify that the max value is found
    def test_max_node(self):
        root_a = BSTNode(10)
        root_a.insert_node(5)
        root_a.insert_node(7)
        root_a.insert_node(3)
        root_a.insert_node(15)
        root_a.insert_node(12)
        root_a.insert_node(17)
        self.assertEqual(17, root_a.max_node().data)
        root_b = BSTNode(10)
        root_b.insert_node(5)
        root_b.insert_node(3)
        root_b.insert_node(7)
        self.assertEqual(10, root_b.max_node().data)

    # Verify that successor gets the next node correctly
    def test_successor_node(self):
        root = BSTNode(10)
        root.insert_node(5)
        root.insert_node(7)
        root.insert_node(3)
        root.insert_node(15)
        root.insert_node(12)
        root.insert_node(17)
        # None when successor doesn't exist
        self.assertIsNone(root.right.right.successor_node())
        # Non-empty right subtree
        self.assertEqual(7, root.left.successor_node().data)
        self.assertEqual(12, root.successor_node().data)
        self.assertEqual(17, root.right.successor_node().data)
        # Empty right subtree
        self.assertEqual(10, root.left.right.successor_node().data)
        self.assertEqual(5, root.left.left.successor_node().data)

    # Verify that predecessor gets the prev node correctly
    def test_predecessor_node(self):
        root = BSTNode(10)
        root.insert_node(5)
        root.insert_node(7)
        root.insert_node(3)
        root.insert_node(15)
        root.insert_node(12)
        root.insert_node(17)
        # None when predecessor doesn't exist
        self.assertIsNone(root.left.left.predecessor_node())
        # All others have a predecessor
        self.assertEqual(3, root.left.predecessor_node().data)
        self.assertEqual(5, root.left.right.predecessor_node().data)
        self.assertEqual(7, root.predecessor_node().data)
        self.assertEqual(10, root.right.left.predecessor_node().data)
        self.assertEqual(12, root.right.predecessor_node().data)
        self.assertEqual(15, root.right.right.predecessor_node().data)

    # Verify that search can find nodes properly
    def test_exist_node(self):
        root = BSTNode(10)
        root.insert_node(5)
        root.insert_node(7)
        root.insert_node(3)
        root.insert_node(15)
        root.insert_node(12)
        root.insert_node(17)
        # Nodes that exist
        self.assertTrue(root.exist_node(3))
        self.assertTrue(root.exist_node(5))
        self.assertTrue(root.exist_node(7))
        self.assertTrue(root.exist_node(10))
        self.assertTrue(root.exist_node(12))
        self.assertTrue(root.exist_node(15))
        self.assertTrue(root.exist_node(17))
        # Nodes that do not exist
        self.assertFalse(root.exist_node(1))
        self.assertFalse(root.exist_node(4))
        self.assertFalse(root.exist_node(11))
        self.assertFalse(root.exist_node(21))
        self.assertFalse(root.exist_node(16))


class RBTreeTest(unittest.TestCase):

    # Verify insert functions as expected on simple tree
    def test_insert_tree_simple(self):
        tree = RBTree()
        self.assertIsNone(tree.sentinel.data)
        self.assertIsNone(tree.root)
        tree.insert(10)
        self.assertEqual(10, tree.root.data)
        self.assertEqual("black", tree.root.color)
        self.assertEqual(tree.sentinel, tree.root.parent)
        tree.insert(5)
        self.assertEqual(10, tree.root.data)
        self.assertEqual("black", tree.root.color)
        self.assertEqual(5, tree.root.left.data)
        self.assertEqual("red", tree.root.left.color)
        tree.insert(7)
        self.assertEqual(7, tree.root.data)
        self.assertEqual("black", tree.root.color)
        self.assertEqual(tree.sentinel, tree.root.parent)
        self.assertEqual(5, tree.root.left.data)
        self.assertEqual("red", tree.root.left.color)
        self.assertEqual(10, tree.root.right.data)
        self.assertEqual("red", tree.root.right.color)

    # Verify that an array of integers is inserted properly
    def test_insert_list_tree(self):
        tree = RBTree()
        array = [10, 5, 15, 3, 7, 12, 16]
        tree.insert_list(array)
        expected_tree = '(3: red), (5: black), (7: red), (10: black), ' \
                        '(12: red), (15: black), (16: red)'
        self.assertEqual(expected_tree, tree.rb_inorder_walk())

    # Further verification of inserting to RBTree
    def test_insert_tree_complex(self):
        tree = RBTree()
        array = [100, 50, 150, 30, 70, -1000, 26, 31, 101, 9000, 25]
        tree.insert_list(array)
        expected_tree = '(-1000: black), (25: red), (26: red), (30: black), ' \
                        '(31: red), (50: black), (70: black), (100: red), ' \
                        '(101: red), (150: black), (9000: red)'
        self.assertEqual(expected_tree, tree.rb_inorder_walk())

    # Verify that the red black tree walk is correct
    def test_rb_inorder_walk(self):
        tree = RBTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        expected_walk = '(5: red), (10: black), (15: red)'
        self.assertEqual(expected_walk, tree.rb_inorder_walk())

    # Verify that the tree height is calculated correctly
    def test_tree_height(self):
        tree = RBTree()
        self.assertEqual(0, tree.tree_height())
        tree.insert(10)
        self.assertEqual(0, tree.tree_height())
        tree.insert(5)
        self.assertEqual(1, tree.tree_height())
        tree.insert(15)
        self.assertEqual(1, tree.tree_height())
        tree.insert(7)
        self.assertEqual(2, tree.tree_height())
        tree.insert(2)
        self.assertEqual(2, tree.tree_height())
        tree.insert(12)
        self.assertEqual(2, tree.tree_height())
        tree.insert(17)
        self.assertEqual(2, tree.tree_height())
        tree.insert(20)
        self.assertEqual(3, tree.tree_height())

    # Verify that the list is in sorted order
    def test_sort_tree(self):
        tree = RBTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(3)
        tree.insert(7)
        tree.insert(12)
        tree.insert(16)
        expected_list = [3, 5, 7, 10, 12, 15, 16]
        self.assertEqual(expected_list, tree.sort())

    # Verify that node existence is detectable
    def test_in_tree(self):
        tree = RBTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(3)
        tree.insert(7)
        tree.insert(12)
        tree.insert(16)
        # Nodes that exist
        self.assertTrue(tree.in_tree(10))
        self.assertTrue(tree.in_tree(5))
        self.assertTrue(tree.in_tree(15))
        self.assertTrue(tree.in_tree(3))
        self.assertTrue(tree.in_tree(7))
        self.assertTrue(tree.in_tree(12))
        self.assertTrue(tree.in_tree(16))
        # Nodes that do not exist
        self.assertFalse(tree.in_tree(21))
        self.assertFalse(tree.in_tree(4))
        self.assertFalse(tree.in_tree(11))

    # Verify that search returns the correct object (memory address)
    def test_search_tree(self):
        tree = RBTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(3)
        tree.insert(7)
        tree.insert(12)
        tree.insert(16)
        # Expect memory address of correct node
        self.assertEqual(tree.root, tree.search(10))
        self.assertEqual(tree.root.left, tree.search(5))
        self.assertEqual(tree.root.left.left, tree.search(3))
        self.assertEqual(tree.root.left.right, tree.search(7))
        self.assertEqual(tree.root.right, tree.search(15))
        self.assertEqual(tree.root.right.left, tree.search(12))
        self.assertEqual(tree.root.right.right, tree.search(16))
        # Expect None when node does not exist
        self.assertIsNone(tree.search(8))
        self.assertIsNone(tree.search(9))
        self.assertIsNone(tree.search(17))

    # Verify the tree min is returned
    def test_min_tree(self):
        tree = RBTree()
        self.assertIsNone(tree.min())
        tree.insert(10)
        self.assertEqual(10, tree.min().data)
        tree.insert(5)
        self.assertEqual(5, tree.min().data)
        tree.insert(15)
        tree.insert(7)
        tree.insert(12)
        tree.insert(16)
        tree.insert(3)
        self.assertEqual(3, tree.min().data)

    # Verify the tree max is returned
    def test_max_tree(self):
        tree = RBTree()
        self.assertIsNone(tree.max())
        tree.insert(10)
        self.assertEqual(10, tree.max().data)
        tree.insert(5)
        tree.insert(15)
        self.assertEqual(15, tree.max().data)
        tree.insert(3)
        tree.insert(7)
        tree.insert(12)
        tree.insert(16)
        self.assertEqual(16, tree.max().data)


def main():
    unittest.main(verbosity=3)


main()
