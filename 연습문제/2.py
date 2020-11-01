n = input()


sum = int(n[0])

for i in range(1,len(n)) :
    temp1 = sum + int(n[i]) 
    temp2 = sum * int(n[i])
    sum = max(temp1,temp2)

print(sum)




