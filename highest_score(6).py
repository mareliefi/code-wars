def high(x):
  string_list = x.split()
  word_total_list = []
  max_index = 0
  for word in string_list:
    word_total = 0
    for letter in word:
      word_total = word_total + (ord(letter)-96)
    word_total_list.append(word_total)
  max_index = (word_total_list.index(max(word_total_list)))
  return(string_list[max_index])
    
