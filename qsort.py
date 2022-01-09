def qsort(L):
    if L==[]: return []
    return qsort([x for x in L[1:] if x<L[0]])+L[0:1]+qsort([x for x in L[1:] if x>=L[0]])
lst=[34,12,56,23,52,50,67,22,45,33,11]
print(qsort(lst))
