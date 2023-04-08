PN=int(input())
num = 0
A_P = list(map(int,input().split()))
seat = []
for i in range(PN):
    if A_P[i] in seat:
        num +=1
    else:
        seat.append(A_P[i])

print(num)



    




    
    