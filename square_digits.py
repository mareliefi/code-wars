def square_digits(num):
  number_list = list(str(num))
  count = 0
  number_string = ""
  for num in number_list:
    number_list[count] = str(int(num)**2)
    number_string = number_string + number_list[count]
    count += 1
  return int(number_string)

