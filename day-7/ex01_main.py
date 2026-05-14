#import ex01_fun
#ex01_fun.hello() #함수호출


#from ex01_fun import *
#hello()


#import ex01_fun as f1 
#f1.hello()


#from ex01_fun import hi
#hi()

#hello()  






from gugu_modul import *



r= True
while r :
   num=int(input("숫자를 선택하세요(1:세로구구단 2:가로구구단 0:종료)"))
   if  num == 1 :
       v_gugudan()


   elif num == 2:
       h_gugudan()


   elif num == 0:
    r =False


   else:
    print("잘못 선택: 다시 입력")

