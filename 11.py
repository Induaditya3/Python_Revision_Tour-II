dict={2:3,1:5} #TO FILL
def BubbleSort(l):
  for i in range(len(l),1,-1):
    for j in range(i-1):
      if l[j]>l[j+1]:
        temp=l[j]
        l[j]=l[j+1]
        l[j+1]=temp
  return l

key=list(dict.keys())
print(BubbleSort(key))