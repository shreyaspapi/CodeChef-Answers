t = int(input())
while t:
    a,b = list(map(int, input().split()))
    if a < b:
        print("<")
    elif a > b:
        print(">")
    else:
        print("=")
    t-=1
