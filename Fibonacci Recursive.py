# 0,1,1,2,3,5,8

def fibonacci(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return fibonacci(i-2)+fibonacci(i-1)
    
index=int(input("Enetr number of sequence: "))
if index <=0:
    print("This is not the valid number")
else:
    for i in range(index):
        print(fibonacci(i))

