n = int(input())

h,m,s = 0,0,0
cnt = 0


## ? 3중 포문 으로 구하면 된다 ?
## ㅋㅋㅋ
while (True):
    
    if s%10 == 3 :
        cnt +=1
    elif (s//10)%10 == 3:
        cnt+=1
    elif m %10 == 3 :
        cnt+=1
    elif (m//10)%10 ==3:
        cnt +=1
    elif (h%10) == 3:
        cnt+=1
    elif (h//10)%1 == 3:
        cnt +=1
    
    
    s+=1
    if s == 60:
        m +=1
        s=0
    if m == 60:
        h +=1
        m=0

    if h == n +1 :
        break    

print(cnt)       
