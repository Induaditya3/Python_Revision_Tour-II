fib=[0,1]
for i in range(7):
  first=fib[-2]
  second=fib[-1]
  fib.append(first+second)
  
print(fib)