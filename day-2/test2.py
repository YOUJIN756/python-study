amrkn=int(input("아메리카노 판매 개수: "))
kprt=int(input("카페라떼 판매 개수: "))
kpchn=int(input("카푸치노 판매 개수: "))

A=amrkn*2000
B=kprt*3000
C=kpchn*3500

hap=A+B+C

print("총 매출은 "+str(hap)+"원 입니다")