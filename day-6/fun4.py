#키워드 인수는 인수의 이름을 명시적으러 

def sub(x,y,z):
    print('x=', x, 'y=',y, 'z=',z, sep="   ")


sub(100,200,300)
sub(y=20, x=10, z=30)
sub(y=55, x=35, z=15)


