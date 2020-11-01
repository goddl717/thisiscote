n = input()
left = 0
right = 0

for i in range(len(n)//2) :
    left += int(n[i])
for i in range(len(n)//2, len(n)):

    right += int (n[i])

print(left,right)
if left == right :
    print("Lucky")
else :
    print("ready")