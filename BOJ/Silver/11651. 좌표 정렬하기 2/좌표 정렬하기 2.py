n = int(input())
ps = [tuple(map(int, input().split())) for _ in range(n)]
for a, b in sorted(ps, key = lambda x: (x[1], x[0])):
  print(a, b)