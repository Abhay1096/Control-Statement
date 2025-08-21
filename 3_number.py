num1 = int(input("Enter the number : "));
num2 = int(input("Enter the number : "));
num3 = int(input("Enter the number : "));

if(num1<num2 and num1<num3):
    print(f"{num1} is the minimum no. among three")

if(num2<num1 and num2<num3):
    print(f"{num2} is the minimum no. among three")

elif(num3<num1 and num3<num2):
    print(f"{num3} is the minimum no. among three")
