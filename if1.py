
#if1.py
st= input("영어 1글자를 입력하세요: ")
if  st.isupper(): #대문자-> true 아니면->false
    print(st.lower())# true일때 수행->소문자로 변경
else:  
    print(st.upper()) # 대문자로 변경








#점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
#사용자로부터 score를 입력받아 학점을 출력하라.
#  점수    학점
#  81~100  A
#  61~80   B
#  41~60   C
#  21~40   D
#  0~20    E

num=int(input("점수를 입력하세요: "))

if num>=0 and num<21:
    print("E")
    
elif num>=21 and num<41:
    print("D")

elif num>=41 and num<61:
    print("C")

elif num>=61 and num<81:
    print("B")

elif num>=81 and num<=100:
    print("A")
















