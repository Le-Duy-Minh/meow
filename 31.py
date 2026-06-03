h,p,s=map(int,input("Nhập giờ, phút, giây:").split())
s1= s+1 
if s1==60:
    p1= p+1
    s1=0
    if p1==60:
        p1=0
        h1= h+1 
        print(h1,p1,s1)
    else:
        print(h,p1,s1)
else: 
     print(h,p,s1)
        