i = 1
while i < 6:
  print(i)
  i += 1
  
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
  
p = 0
while p < 6:
  p += 1
  if p == 3:
    continue
  print(p)
  

a = 1
while a < 6:
  print(a)
  a += 1
else:
  print("a is no longer less than 6")