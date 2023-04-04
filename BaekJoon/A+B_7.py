T = input()
C=[]

for _ in range(int(T)):
    A,B = map(int ,input().split())
    C.append(A+B) 
for i in range(int(T)):
    print("Case#",i+1,": ",C[i])

