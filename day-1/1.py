
# input: 키보드로부터 입력("출력문자")
# input은 기본적으로 입력받는 것을 문자로 인식함
# 정수로 입력하고자 하면 괄호치고 그 앞에 int를 붙임


# 간단한 실습
n = "apple"
print("I like", n)
print("I like"+ n)
print(3+5)
# print에서 ,는 구분&공백    +는 문자일 땐 연결, 숫자일 땐 더하기
# print("결과는 "+20) # <- 오류
# +는 문자끼리, 숫자끼리 가능



# input 실습
a=int(input("숫자1 입력: "))
b=int(input("숫자2 입력: "))
sum=a+b
print(sum)

name=input("이름 입력: ")
print(name)