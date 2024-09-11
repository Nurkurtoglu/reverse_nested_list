def flattenFon(l):
    # l = [1, 2, 3, [9, 8, 7], ["a"], ["b"]]

    # isinstance(l[3], list)
    l1 = []
    for i in l:
        if isinstance(i, list):
            l1.extend(i)
        else:
            l1.append(i)
    return l1

liste = [1, 2, 3, [9, 8, 7], ["a"], ["b"]]
print(flattenFon(liste))