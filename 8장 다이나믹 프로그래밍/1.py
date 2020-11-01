# 이 문제가 dp라고?
# 탑 다운 방식으로 문제를 풀 수 있다.
# 버튼 업 방식으로도 문제를 풀 수 있다.
# 약간 애매하네 ? 내가 문제를 어떻게 풀지에 관한 애매하다....

dp= [-1] * 300001
def rec(value,cnt) :
    if value == 1 :
        return cnt
    if (dp[value] != -1) :
        return dp[value]
    ret = 9876543421

    if value % 5 ==0 :
        ret  = min (ret,rec( value//5,cnt+1))
    if value % 3 == 0 :
        ret = min (ret,rec( value//3,cnt+1))
    if value %2 == 0 :
        ret = min (ret,rec( value//2,cnt+1))
    ret = min (ret, rec(value-1,cnt+1))
    
    dp[value] = ret
    return ret

print(rec(1000,0))
