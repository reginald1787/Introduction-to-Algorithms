Class TreeNode:
  def __init__(self,val,c):
    self.val = val
    self.color = c
    self.left = None
    self.right = None
    self.parent = None
    
    
def leftRotate(root,node):
  right = node.right
  node.right = right.left
  if right.left :
    right.left.parent = node
  right.parent = node.parent
  if not node.parent:
    root = right
  elif node == node.parent.left:
    node.parent.left = right
  else:
    node.parent.right = right
  right.left = node
  node.parent = right
    
