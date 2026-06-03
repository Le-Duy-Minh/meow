a,b,m,c,d,n=map(int,input("Nhập a b m c d n=").split())
D= a*d-c*b
Dx= d*m-n*b
Dy= a*n-m*c
if D!=0:
    x=Dx/D
    y=Dy/D
    print("x=",x,"y=",y)
else:
    print("pt vô nghiệm hoặc vô số nghiệm")