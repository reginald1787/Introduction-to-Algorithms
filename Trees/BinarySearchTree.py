Class TreeNode:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None
    self.parent = None
  
def inOrder(root):
  if root:
    inOrder(root.left)
    print root.val
    inOrder(root.right)
    
    
def search(root,key):
  if not root or root.val==key:
    return root
  if key<root.val:
    return search(root.left,key)
  else:
    return search(root.right,key)
    
def minimum(root):
  p  = root
  while p.left:
    p = root.left
  return p 
  
def maximum(root):
  p  = root
  while p.right:
    p = root.right
  return p 
  
def successor(node):
  if node.right:
    return minimum(node.right)
  p = node.parent
  q = node
  while p and q == p.right:
    q = p
    p = q.parent
  return p
  
def predecessor(node):
  if node.left:
    return maximum(node.left)
  p = node.parent
  q = node
  while p and q == p.left:
    q = p
    p = q.parent
  return p
  
  
  
