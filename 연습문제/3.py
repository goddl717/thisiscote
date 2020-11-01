n = input()
s0 = 0
s1 = 0
n = list(n)
n.append('3')
n = ''.join(n)


for i in range(len(n)):
    if n[i] =='0' and n[i+1] != '0':
        s0 +=1
    if n[i] =='1' and n[i+1] != '1':
        s1 +=1

print(min(s0,s1))

    