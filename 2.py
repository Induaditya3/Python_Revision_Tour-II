sentences=input("Enter sentences: ").strip()
words=sentences.split()

no_of_char=0
no_alphanum=0

for char in sentences:
  no_of_char+=1
  if char.isalnum():
    no_alphanum+=1

print('-'*38)
print(f'No of words={len(words)} \nNo of characters={no_of_char}\nPercentage of alpha numeric characters={(no_alphanum/no_of_char)*100}')