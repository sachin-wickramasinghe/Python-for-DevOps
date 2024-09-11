a=121
b=str(a)
c=int(b)+1
rev=""
for i in b:
    rev=i+rev
print(int(rev)==a)