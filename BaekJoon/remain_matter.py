A ,B,C= map(int,input().split())

A =int(A)
B = int(B)
C = int(C)

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print((A%C)*(B%C)%C)

#map 함수를 이용해서 3개의 값을 받기. 
#print(f) 이용하기