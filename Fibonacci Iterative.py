# 0,1,1,2,3,5,8

index=int(input("Enetr number of sequence: "))

first_num = 0
second_num = 1
temp=0


if index==1:
    print(first_num)
elif index==2:
    print(first_num)
    print(second_num)
elif index<0:
    print("error index")
else:
    print(first_num)
    print(second_num)
    for i in range(index-2):
        temp=first_num+second_num
        print(temp)
        first_num=second_num
        second_num=temp

