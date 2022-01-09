def get_missingnum(lst):
    return set(range(lst[len(lst)-1])[1:])-set(l)
l=list(range(1,100))
l.remove(49)
print(get_missingnum(l))
