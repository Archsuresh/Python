def intersect(lst1,lst2):
    res, lst2_cpy=[],lst2[:]
    for el in lst1:
        if el in lst2_cpy:
            res.append(el)
            lst2_cpy.remove(el)
    return res
list1=[2,4,6,7,4,6,76,8]
list2=[4,57,89,7,4,6,6,3]
print(intersect(list1,list2))
