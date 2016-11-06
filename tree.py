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
