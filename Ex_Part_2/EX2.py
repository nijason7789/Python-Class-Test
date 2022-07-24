n = input()
x = list(n)
ans = 0

for i in range(len(n)):
    ans = ans + int(x[i])

print(ans)