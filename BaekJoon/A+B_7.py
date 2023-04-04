"""T = input()
C=[]

for _ in range(int(T)):
    A,B = map(int ,input().split())
    C.append(A+B) 
for i in range(int(T)):
    print("Case #{}: {} + {} = {}".format(i+1, A, B, C[i]))
"""

t = int(input())

for i in range(1, t+1):  # 1부터 t까지
    a, b = map(int, input().split())
    print(f'Case #{i}: {a+b}')

