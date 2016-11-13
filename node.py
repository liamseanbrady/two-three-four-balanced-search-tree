class Node:
  def __init__(self, keys):
    self.keys = keys
    self.parent = None
    self.left_child = None
    self.left_middle_child = None
    self.right_middle_child = None
    self.right_child = None

  def add_left_child(self, node):
    self.right_child = node
    node.parent = self

  def add_left_middle_child(self, node):
    self.left_middle_child = node
    node.parent = self

  def add_right_middle_child(self, node):
    self.right_middle_child = node
    node.parent = self

  def add_right_child(self, node):
    self.right_child = node
    node.parent = self

  def is_leaf(self):
    return self.left_child == None and \
    self.left_middle_child == None and \
    self.right_middle_child == None and \
    self.right_child == None
