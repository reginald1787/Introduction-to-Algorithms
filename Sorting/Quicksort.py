


def Partition(arrary, start, end):
  x = array[end]
  i = start - 1
  for j in range(start, end):
    if array[j]<=x:
      i+=1
      (array[i],array[j]) = (array[j],array[i])
  (array[i+1],array[end]) = (array[end],array[i+1])
  return i+1


def Quicksort(array, start, end):
  if start<end:
    pivot = Partition(array, start, end)
    Quicksort(array, start, pivot-1)
    Quicksort(array, pivot+, end)
