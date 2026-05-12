#재귀 호출(함수 내부에서 자기자신을 호출)
#5!(팩토리얼)
def fact(n): #fact:함수명(매개변수는 1개)
    if n == 1:
        return 1
    else:
        return n* fact(n-1) # 5*fact(4)= 5 * 24 =120
                            # 4*fact(3)= 4 * 6 =24
                            # 3*fact(2)= 3 * 2 =6
                            # 2*fact(1)= 2 * 1 =2
    

a=int(input("정수를 입력해주세요: ")) 
res=fact(a) #함수 호출, 인수 a(정수) 보냄
#반환되어서 온 결과물 res 저장
print(a, "!는",res,"이다")











def hap(n):
    if n == 0:
        return 1
    else:
        return n+ hap(n-1)


b=int(input("정수 입력: "))
ees=hap(b)
print(b, "!는", ees, "이다")

