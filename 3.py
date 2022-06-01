L=eval(input('L='))
M=eval(input('M='))
size=len(L)
if size==len(M):
  N=[L[i]+M[i] for i in range(size)]
else:
  print('Lists of different sizes.')
print('N=',N)