def find_pairs(l,x):
    pairs=[]
    for (i,el_1)in enumerate(l):
        for (j,el_2)in enumerate(l[i+1:]):
            if el_1+el_2==x:
                pairs.append((el_1,el_2))
    return pairs

list=[2,4,5,6,8]
sum=7
print(find_pairs(list,sum))
        
