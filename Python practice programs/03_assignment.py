l1 = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

res = []

set = set()
for i in l1:
    if i not in set:     
        set.add(i)       
        res.append(i) 
print(res)