#함수

def add(a, b): #()안에는 매개변수
    return a+b


n1=int(input("숫자1 입력"))
n2=int(input("숫자2 입력"))
sum1=add(n1,n2)

print(sum1)



#sum():합계
#len():길이

def avg(numbers): #함수 선언
      if not numbers:
           return 0
      total=sum(numbers) #합계
      cnt=len(numbers) #길이(개수)
      return total/cnt #평균 구하여 반환(리턴)


score_list=[80,90,100,50,70]
aver_res=avg(score_list) #함수 호출, 반환된 값을 저장
print(aver_res) #평균 출력







