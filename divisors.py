def divisors(integer):
  divs = []
  if integer > 3:
    for num in range(2,integer):
      if integer % num == 0:
        divs.append(num)
    if len(divs) == 0:
      return "%d is prime" % integer
    else:
      return divs
  else:
    return "%d is prime" % integer      