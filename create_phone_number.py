def create_phone_number(n):
    phone_number = []
    for number in n:
      phone_number.append(number)
    phone_number.insert(0,'(')
    phone_number.insert(4,')')
    phone_number.insert(5,' ')
    phone_number.insert(9,'-')
    return ''.join(str(e) for e in phone_number)

