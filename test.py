t = (1,1,1,2,3,4,4)

k = 0
g = []
for i in t:
    sum = 0
    for j in t:
        
        if j==i and (not j in g)  :
            sum+=1
    if sum>1:
        k+=1
        g+=[i]


print(k)
        
