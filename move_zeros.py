def move_zeros(array):
  new_array = []
  count = -1
  for i in array:
    if isinstance(i,str) == False and (str(i) == "0" or str(i) == "0.0"):
      new_array.append(i)
    else:
      count += 1
      new_array.insert(count,i)
  return new_array

