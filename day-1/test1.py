name=input("상품 이름 입력: ")
price=int(input("상품 가격 입력: "))
quan=int(input("상품 수량 입력: "))

hap=price*quan
print(name,"의 총 가격은",hap,"원입니다")
print(name+"의 총 가격은 "+str(hap)+"원입니다")
print(f"{name}의 총 금액은 {hap}원 입니다")
# print 안에서 f는 f-string 이라하며 포맷 문자열
#  => f"{변수 값}"

# str : 숫자->문자로 변환
# 실수는 float만 있음(8바이트)