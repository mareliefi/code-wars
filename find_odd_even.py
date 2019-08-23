def find_outlier(integers):
    array_even = []
    array_odd = []
    for i in integers:
        if i % 2 == 0:
            array_even.append(i)
        else:
            array_odd.append(i)
    if len(array_even) == 1:
        return array_even[0]
    else:
        return array_odd[0]
    