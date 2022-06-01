def addDict(dict1,dict2):
  return {**dict1,**dict2}
'''
Alternative definition
def addDict(dict1,dict2):
  newDict={}
  for key,val in dict1.items():
      newDict[key]=val
  for key,val in dict2.items():
      newDict[key]=val
  return newDict
'''      
x={1:2,3:5} # TO FILL
y={1:0,6:5} # TO FILL
print(addDict(x,y))