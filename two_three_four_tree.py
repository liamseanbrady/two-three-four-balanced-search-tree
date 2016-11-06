class Node:
  def __init__(self, keys):
    self.keys = keys
    self.left_child = None
    self.left_middle_child = None
    self.right_middle_child = None
    self.right_child = None

  def add_left_middle_child(self, node):
    self.left_middle_child = node

  def add_right_middle_child(self, node):
    self.right_middle_child = node

  def add_right_child(self, node):
    self.right_child = node

  def is_leaf(self):
    return self.left_child == None and \
    self.left_middle_child == None and \
    self.right_middle_child == None and \
    self.right_child == None

class Tree:
  def __init__(self, root_node):
    self.root = root_node

  def find(self, key):
    current_node = self.root
    current_node_keys = current_node.keys
    while not current_node.is_leaf():
      if key in current_node.keys:
        return key
      else:
        if len(current_node_keys) == 1:
          if key < current_node_keys[0]:
            if current_node.left_child != None:
              current_node = current_node.left_child
            else:
              return None
          else:
            if current_node.right_child != None:
              current_node = current_node.right_child
            else:
              return None
        elif len(current_node_keys) == 2:
          if key < current_node_keys[0]:
            if current_node.left_child != None:
              current_node = current_node.left_child
            else:
              return None
          elif key < current_node_keys[1]:
            if current_node.left_middle_child != None:
              current_node = current_node.left_middle_child
            else:
              return None
          else:
            if current_node.right_child != None:
              current_node = current_node.right_child
            else:
              return None
        else:
          if key < current_node_keys[0]:
            if current_node.left_child != None:
              current_node = current_node.left_child
            else:
              return None
          elif key < current_node_keys[1]:
            if current_node.left_middle_child != None:
              current_node = current_node.left_middle_child
            else:
              return None
          elif key < current_node_keys[2]:
            if current_node.right_middle_child != None:
              current_node = current_node.right_middle_child
            else:
              return None
          else:
            if current_node.right_child != None:
              current_node = current_node.right_child
            else:
              return None
    if key not in current_node.keys:
      return None 
    else:
      return key
