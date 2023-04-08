N = int(input())
X=[]
Y =[]
for _ in range(N):
    A,B=map(int,input().split())
    X.append(A)
    Y.append(B)

MAX_X = max(X)
MIN_X = min(X)

MAX_Y = max(Y)
MIN_Y = min(Y)

print(((MAX_X)-(MIN_X))*((MAX_Y)-(MIN_Y)))

