#for i in range(6)
#=>0~5 6번 반복

snack={
"새우깡":3000,
"매운 새우깡":3500,
"양파링":4000
}
for i in snack:
    print(i) #키 값만 출력
for j in snack.items():
    print(j)
for k in snack.values():
    print(k)

#리스트
fruit=["파인애플","참외","배","오렌지","골드키위"]
cart=[]
for i in fruit:
    if len(i) <=3:
        cart.append(i)

print(cart)




##################################################

import sys
user_pass = input("패스워드를 입력하시오(영어3자): ")
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z']
for letter1 in password:
        for letter2 in password:
            for letter3 in password:
                guess = letter1+letter2+letter3
                print(guess)
                if guess == user_pass:
                    print("당신의 패스워드는 "+guess)
                    sys.exit() #즉시 중지









                    