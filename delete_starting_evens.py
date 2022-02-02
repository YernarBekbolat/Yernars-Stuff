def delete_starting_evens(first):
  while (len(first) > 0 and first[0] % 2 == 0):
    first = first[1:]
  return first
    
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#Удаляет все чётные цифры в листе, пока не наткнётся до нечётного числа или лист не опустеет