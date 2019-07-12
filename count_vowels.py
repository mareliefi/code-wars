def getCount(inputStr):
  num_vowels = 0
  for letter in inputStr:
    if letter in "aeiouAEIOU":
      num_vowels += 1
  return num_vowels

