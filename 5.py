list_of_words=['HI','Heyo','ciao'] #TO FILL
length=len(list_of_words[0])
largest=list_of_words[0]
for i in range(1,len(list_of_words)):
  new=len(list_of_words[i])
  if length<new:
    length=new
    largest=list_of_words[i]

print('The largest word=',largest)
    