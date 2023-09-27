def linearSearchProtect(productlist,targetproduct):
  indices=[]
  for index,product in enumerate(productlist):
   if product==targetproduct:
    indices.append(index)
  return indices
product =["cat","dog","cat","horse","cat","penguin","beetle"]
target ="cat"
target1="lion"
result=linearSearchProtect(product,target)
print(result)

