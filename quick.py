def quick(a,l,u):
  key=a[l]
  low=l+1
  high=u
  if low<=high:
    while key>a[low]:
      low+=1
    while key<a[high]:
      high-=1
    if low<high:
      t=a[low]
      a[low]=a[high]
      a[high]=t
  if low>high:
    t=key
    key=a[high]
    a[high]=t
  if high-1>l:
    quick(a,l,high-1)
  if high+1<u:
     quick(a,high+1,u)
  return a
print quick(a=[12,3,67,23,21,96,34],0,len(a)-1)












  
