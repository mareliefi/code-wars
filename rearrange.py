def spin_words(sentence):
  sentence_list = sentence.split()
  new_word = ""
  for counter in range(0,len(sentence_list)):
    new_word = ""
    if len(sentence_list[counter]) < 5:
      sentence_list[counter] = sentence_list[counter]
      counter += 1
    else:
      i = len(sentence_list[counter])-1
      while i>-1:
        new_word = new_word + sentence_list[counter][i]
        i -= 1
      sentence_list[counter] = new_word
      counter += 1
  return " ".join(sentence_list)
 



