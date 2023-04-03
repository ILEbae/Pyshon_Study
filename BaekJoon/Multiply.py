"""A=int(input())
B=list(input())

C=[]

for i in reversed(B):
    i=int(i)
    mul = A*i
    print(mul)
    C.append(mul)

B=B[:]
print(B)
"""

A=int(input())
B=input()

AxB2 = A * int(B[2])
AxB1 = A * int(B[1])
AxB0 = A * int(B[0])
AxB = A* (int(B))


print(AxB2,AxB1,AxB0,AxB,sep='\n')

##1. list에서 꺼낸후 int 로 변환해주는 생각을 하지못하였다.
##2. list 안을 for 문에서 역순으로 뽑고싶을때 reverse를 사용하면 된다.
##3. append 라는 함수는 리스트 안에 뒤에서부터 차곡 차곡 쌓이는 함수이다.
##4. sep을 사용하여 , 마다 개행한다.

