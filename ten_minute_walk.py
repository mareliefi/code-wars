def isValidWalk(walk):
    distance = len(walk)
    n = [0,0]
    if distance != 10:
        return False
    else:
        for direction in walk:
            if direction.lower() == 'n':
                n[1] = n[1] + 1
            elif direction.lower() == 's':
                n[1] = n[1] - 1
            elif direction.lower() == 'e':
                n[0] = n[0] + 1
            else:
                n[0] = n[0] - 1
        if n[0] == 0 and n[1] == 0:
            return True
        else:
            return False
            