def transform_list(x):
    a=[]
    b=x.split()
    for i in (b):
        i = int(i)
        y=2*i**3+3*i+1
        a.append(y)
    return a
if __name__=="__main__":
    x=input()
    print(transform_list(x))
    
    