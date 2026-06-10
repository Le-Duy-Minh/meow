print("Nhập số M<N: ")
m=int(input("Nhập M:"))
n=int(input("Nhập N:"))
a=0
for i in range (m,n+1):
    if i%3==0 or i%5==0:
        a=i+a
print("Kết quả: ",a)
        