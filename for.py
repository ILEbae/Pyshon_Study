"""
for문의 기본 구조

for 변수 in 리스트(튜플 or  문자열):
    수행할문장1
    수행할문장2
    ...
"""


"""test_list = ['one' , 'two' , 'three']
for i in test_list:
    print(i)
    """


"""
a = [(1,2),(3,4),(5,6)]
for(first, last) in a:
    print(first+last)

    ##cf) 튜플 --> (a,b) = (1,2)
"""



"""
marks = [90,25,67,45,80]
number = 0

for mark in marks :
    number += 1
    if mark >=60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)
"""

##for 문과 continue

"""
marks = [90,25,67,45,80]
number = 0

for mark in marks :
    number += 1
    if mark <60: continue
    
    print("%d번 학생은 합격입니다." %number)
"""      


##range  함수와  for 같이 사용하기

"""sum = 0
for i in range(1,11):
    print(i)
print(sum)"""

"""add = 0 
for i in range(1,11):
    add = add+i
print(add)"""


"""marks = [90,25,67,45,80]
for number in range(len(marks)):
    if marks[number]<60:
        continue
    print("%d 번 학생 축하합니다. 합격입니다."%(number+1))
"""
## len 함수 => 리스트 안의 요소 개수를 돌려주는 함수이다. len(marks)= 5 를 반환한다.
## number = 0,1,2,3,4 대입



## for 와 range 를 이용한 구구단
"""for i in range(2,10):
    for j in range(1,10):
        print(i*j,end =" ")
    print('')
"""
    ##end 파라미터.=> 다음줄로 넘기지않고 쭉 가기 위해

##리스트 컴프리헨션 사용하기
    ##=> 리스트 안에 for 문을 포함하는 (=리스트 컴프리헨션)


"""
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)
"""
##--> 컴프리헨션 사용후
"""
a = [1,2,3,4]
result = [num*3 for num in a]
print(result)
"""
"""
a = [1,2,3,4]
result = [num*3 for num in a if num%2==0] ## 1. num에 a가 저정된다. 2. num을 3배한다. 3. 짝수만 저장한다.
print(result)
"""


