

num1=int(input("3의 배수 입력: "))
num2=int(input("5의 배수 입력: "))


#브레이크 필요 없음?
match num1%3, num2%5 :
   case 0,0:
       print("num1은 3의 배수 num2는 홀수")

   case 0,_:
        print("num1은 3의 배수 num2는 아무 숫자")

   case _,0:
        print("num2는 5의 배수 num1은 아무 숫자")
        
   case _:
        print("둘다 오류")

