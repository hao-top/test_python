# Author:Mr浩

dfd={"hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhd"}
count=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j !=k and i!=k:
                print(i,k,j)
                count+=1

print(count)


