def toJadenCase(string):
  string_list = string.split(" ")
  for i in range(0,len(string_list)):
    string_list[i] = string_list[i].capitalize()
  print " ".join(string_list) 

