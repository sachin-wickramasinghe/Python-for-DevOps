#swap two number without third variable

a=int(input("Enter a  Number:"))
b=int(input("Enter b Number:"))

print("Variable a before swaping:",a)
print("Variable b before swaping:",b)

#changing logic

a=a+b
b=a-b
a=a-b

print("Variable a after swaping:",a)
print("Variable b after swaping:",b)
