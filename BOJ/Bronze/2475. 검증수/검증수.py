ns = list(map(int, input().split()))

sum = 0
for n in ns:
  sum += n**2

print(sum%10)