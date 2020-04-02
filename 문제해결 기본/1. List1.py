a = int(input())
for i in range(a):
    b = int(input())
    clist = list(map(int, input().split()))
    print(f"#{i+1} {max(clist)- min(clist)}")