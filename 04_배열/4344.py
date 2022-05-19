n = int(input())

for i in range(n):
    num_list = list(map(int, input().split()))
    avg = sum(num_list[1:])/num_list[0]
    cnt = 0
    for num in num_list[1:]:
        if num > avg:
            cnt += 1
    rate = cnt/num_list[0]*100
    print(f'{rate:.3f}%')  