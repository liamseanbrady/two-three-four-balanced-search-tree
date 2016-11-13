import unittest
from node import Node
from tree import Tree

class BalancedSearchTreeTest(unittest.TestCase):
  def test_finds_key_in_the_tree_with_depth_one_and_one_key_root(self):
    root_node = Node([1])
    tree = Tree(root_node)
    result = tree.find(1)

    self.assertEqual(result, 1)

  def test_finds_key_in_the_tree_with_depth_one_and_two_key_root(self):
    root_node = Node([1, 3])
    tree = Tree(root_node)
    result = tree.find(3)

    self.assertEqual(result, 3)

  def test_finds_key_in_the_tree_with_depth_one_and_three_key_root(self):
    root_node = Node([1, 3, 8])
    tree = Tree(root_node)
    result = tree.find(8)

    self.assertEqual(result, 8)

  def test_finds_key_in_the_tree_with_depth_two(self):
    root_node = Node([1, 3, 8])
    target_node = Node([5])
    root_node.add_right_middle_child(target_node)
    tree = Tree(root_node)
    result = tree.find(5)

    self.assertEqual(result, 5)

  def test_finds_key_in_the_tree_with_depth_two_with_two_keys_at_leaf(self):
    root_node = Node([1, 3, 8])
    target_node = Node([9])
    other_node = Node([5])
    root_node.add_right_middle_child(other_node)
    root_node.add_right_child(target_node)
    tree = Tree(root_node)
    result = tree.find(9)

    self.assertEqual(result, 9)

  def test_finds_key_in_the_tree_with_depth_two_with_three_keys_at_leaf(self):
    root_node = Node([1, 3, 8])
    target_node = Node([9])
    other_node = Node([5])
    another_node = Node([2])
    root_node.add_left_middle_child(another_node)
    root_node.add_right_middle_child(other_node)
    root_node.add_right_child(target_node)
    tree = Tree(root_node)
    result = tree.find(2)

    self.assertEqual(result, 2)

  def test_does_not_find_key_in_the_tree_with_depth_two(self):
    root_node = Node([1, 3, 8])
    target_node = Node([5])
    root_node.add_right_middle_child(target_node)
    tree = Tree(root_node)
    result = tree.find(6)

    self.assertEqual(result, None)

  def test_cannot_find_a_key_in_the_tree(self):
    root_node = Node([1, 3, 8])
    tree = Tree(root_node)
    result = tree.find(5)

    self.assertEqual(result, None)

  def test_restructuring_three_key_node(self):
    root_node = Node([9, 16])
    three_key_node = Node([5, 6, 7])
    root_node.add_left_child(three_key_node)
    tree = Tree(root_node)
    tree.restructure_three_key_node(three_key_node)

    self.assertEqual(root_node.keys, [6, 9, 16])
    self.assertEqual(root_node.left_middle_child, 7)
    self.assertEqual(root_node.left_child, 5)
    
if __name__ == '__main__':
  unittest.main()
