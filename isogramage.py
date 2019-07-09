def is_isogram(word):
  word = word.lower()
  for letter in word:
    total = 0
    print letter
    for  symbol in word:
      print symbol
      if letter == symbol:
        total += 1
        if total > 1:
          print False
          break
  print True
  


