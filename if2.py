# 주민번호 입력
# 1,3 -> 남자 아니면 2,4 -> 여자


jumin=input("주민번호 입력: ") #081212-321111
num=jumin.split("-")[1]

#081212 ->[0]
#321111 ->[1] ->num

if num[0] =='1' or num[0] =='3':
#(jumin[7]=='1' or jumin[7]=='3'):
   print("남자")

else:
   print("여자")







   num1=int(input("숫자1을 입력하세요: "))
   num2=int(input("숫자2을 입력하세요: "))
   num3=int(input("숫자3을 입력하세요: "))

if num1 >= num2 and num1>=num3 :
   print("큰수는: ",num1)


elif num2 >= num1 and num2>=num3 :
     print("큰수는: ",num2)


else:
     print("큰수는: ",num3)






