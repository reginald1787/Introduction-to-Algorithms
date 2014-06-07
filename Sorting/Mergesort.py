
def merge(A, start, mid, end):
  n1 = mid - start
  n2 = end - mid
  left = [A[start+i] for i in range(n1)]
  right = [A[mid+j] for j in range(n2)]
  i=0
  j=0
  for k in range(start,end):
    if left[i]<right[j]
      A[k] = left[i]
      i+=1
    else:
      A[k] = right[j]
      j+=1
      
      
def mergesort(A,start,end):
  if start<end:
    mid = (start+end)/2
    mergesort(A,start,mid)
    mergesort(A,mid+1,end)
    merge(A,start,mid,end)
