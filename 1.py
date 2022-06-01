phone=input("Enter the phone number: ")
condition=0

for i in range(len(phone)):
  if (i==3 or i==7) and phone[i]=='-':
    condition+=1
  elif phone[i].isdigit():
    condition+=1
    
if condition==12:
  print('Valid')
else:
  print('Invalid')