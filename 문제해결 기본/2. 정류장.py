a = int(input())

for A in range(1, a +1):
    k, n, m = map(int, input().split())
    m1 = list(map(int, input().split()))
    mlist = [0] * n
    for i in m1:
        mlist[i] += 1
    
    start = 0
    end = k
    cnt = 0


    while True:
        zero = 0
        for i in range(start+1, end + 1):
            if mlist[i] == 1:
                start = i
            else:
                zero += 1

        if zero == k:
            cnt = 0
            break

        cnt += 1
        end = start + k

        if end >= n:
            break



    print(f"#{A} {cnt}")

