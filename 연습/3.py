from itertools import permutations

n=1000000
ret = 0
a = [False,False] + [True]*(n-1)
primes=[]
#FAlSE면 소수가 아님
#TRUE면 소수.
for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

numbers = "011"
print(list(permutations(numbers,1)))
print(list(permutations(numbers,2)))
for i in range(1,len(numbers)+1):
    temp = list(permutations(numbers,i))
    for j in temp:
        temp2 = ''.join(j)
        print(temp2)
        if a[int(temp2)] == True:
            a[int(temp2)] = False
            ret+=1
        
print(ret)









