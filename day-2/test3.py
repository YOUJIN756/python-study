inmoney=int(input("투입한 돈: "))
price=int(input("물건 값: "))

up = inmoney-price
print("거스름 돈: ",up)

coin500s = up // 500
up = up % 500
coin100s = up // 100

print("500원 동전의 개수: ", coin500s)
print("100원 동전의 개수: ", coin100s)

