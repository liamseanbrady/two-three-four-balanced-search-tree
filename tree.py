class Tree:
  def __init__(self, root_node):
    self.root = root_node

  def find(self, key):
    node = self._traverse_nodes(key, self.root)
    return self._find_key_in_node(key, node)

  def restructure_three_key_node(self, node):
    parent_node = node.parent
    middle_key = node.keys.pop(1)

    if middle_key > max(parent_node.keys):
      parent_node.keys.append(middle_key)
    elif middle_key < min(parent_node.keys):
      parent_node.keys.insert(0, middle_key)
    else:
      parent_node.keys.insert(1, middle_key)
    
    parent_node.left_child = node.keys[0]
    parent_node.left_middle_child = node.keys[1]

  def _find_key_in_node(self, key, node):
    if key in node.keys:
      return key
    else:
      return None

  def _traverse_nodes(self, key, node):
    while not node.is_leaf():
      if key < node.keys[0]:
        if node.left_child != None:
          node = node.left_child
      elif key < node.keys[1]:
        if node.left_middle_child != None:
          node = node.left_middle_child
      elif key < node.keys[2]:
        if node.right_middle_child != None:
          node = node.right_middle_child
      else:
        if node.right_child != None:
          node = node.right_child

      if key in node.keys:
        break

    return node
