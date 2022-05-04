n = int(input())

i = 0
c = []

while i < n:
    a, b = map(int, input().split())
    c.append(a+b)
    i += 1

for x in c:
    print(x)