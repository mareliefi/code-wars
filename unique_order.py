def unique_in_order(iterable):
  letter_list = []
  if len(iterable) > 0:
    letter_list.append(iterable[0])
    n = 0
    for letter in iterable:
      if letter_list[n] != letter:
        letter_list.append(letter)
        n += 1
    return letter_list
  else:
    return letter_list


