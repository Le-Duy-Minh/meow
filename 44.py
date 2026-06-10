n=int(input("Nhập N:"))
a=[]
for i in range (1,n+1):
    i=int(input("nhập số thứ "+str(i)+" ="))
    if i>10 and i<20:
        a.append(i)
print("Số các số >10 và <20 là: ",len(a))