import math 
r=int(input("Nhap ban kinh R: "))
x0,y0=map(int,input("Nhap toa do tam duong tron: x0 y0").split())
xa,ya=map(int,input("Nhap toa do diem a:  xa ya").split())
if r >= math.sqrt((xa-x0)**2+(ya-y0)**2):
    print("Diem A nam trong duong tron")
else:
    print("Diem A khong nam trong duong tron")
