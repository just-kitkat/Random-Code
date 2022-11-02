def countRange(list_, min, max):
  updated_list = []
  for i in list_:
    if min <= i <= max:
      updated_list.append(i)

  return len(updated_list)

# TEstING
print(countRange([1,2,3,4,5,6,7,8,7,6,5,4,3,2,1], 3, 6))
print(countRange([1.3, 6.5, 6.8, 65.6, 3.5], 3, 6))