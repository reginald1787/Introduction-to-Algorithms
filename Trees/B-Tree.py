Class TreeNode:
  def __init__(self,keys,isleaf):
    self.keys = keys # nondecreasing array
    self.n = len(keys)
    self.leaf = isleaf # True if is leaf
    if not isleaf:
      self.child = [None for i  in range(n+1)]
      
      
      
def search(root,key):
  i = 0
  while i<root.n and key > root.keys[i]:
    i+=1
  if i<root.n and key == root.keys[i]:
    return (root,i)
  elif x.leaf:
    return 
  else:
    return search(root.child[i],key)
    
    
