nums=[1,2,3,3,4]
counts=[0]*(len(nums)+1)
print(counts)
for i in nums:
  counts[i]+=1
duplicate=-1
missing=-1
for j in range(1, len(counts)):
  if counts[j]==2:
    duplicate=j
  elif counts[j]==0:
    missing=j
print(duplicate, missing)