
def sum_with_range(min, max):
  print(min, max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

result = sum_with_range(1, 5)
print(result)
result_2 = sum_with_range(result, result + 10)
print(result_2)

def sign(num):
  if num > 0:
    return 1
  elif num == 0:
    return 0
  else:
    return -1

print(sign(-5))


