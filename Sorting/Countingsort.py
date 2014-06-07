
def Countingsort(A):
  minA = min(A)
  maxA = max(A)
  k = max(A) - min(A)
  C = [0 for i in range(k+1)]
  for i in range(len(A)):
    C[A[i]]+=1
  for i in range(1,k+1):
    C[i]+=C[i-1]
  res = [0 for i in range(len(A))]
  for i in range(len(A)-1,-1,-1):
    res[C[A[i]]] = A[i]
    C[A[i]]-=1
    
  return res
