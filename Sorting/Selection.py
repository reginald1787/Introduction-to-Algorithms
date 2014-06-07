def Partition(arrary, start, end):
  x = array[end]
  i = start - 1
  for j in range(start, end):
    if array[j]<=x:
      i+=1
      (array[i],array[j]) = (array[j],array[i])
  (array[i+1],array[end]) = (array[end],array[i+1])
  return i+1
  
  
  
def Select(A,start,end,k) # select kth smallest element
  if start == end:
    return A[start]
  pivot = Partition(A,start,end)
  i = pivot-start+1
  if i==k:
    return A[pivot]
  elif i<k:
    return Select(A,pivot+1,end,k-i)
  else:
    return Select(A,start,pivot,k)
