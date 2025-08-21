angle1=int(input("enter first angle"))
angle2=int(input("enter second angle"))
angle3=int(input("enter third angle"))

sum=angle1+angle2+angle3
if(sum==90):
    print("this is a right angle")
elif(sum>90&sum<180):
    print("this is a obtuse angle")
else:
    print("this is acute angle")