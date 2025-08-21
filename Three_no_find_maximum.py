a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
c = int(input("Enter the number : "))

if(a>b & a>c):
    print(f"{a} is maximum number")
elif(b>a & b>c):
    print(f"{b} is maximum number")
else:
    print(f"{c} is maximum number")