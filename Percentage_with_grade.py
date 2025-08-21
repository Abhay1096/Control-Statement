per = int(input("Enter your percentage : "))

if(per<25):
    print("D")
elif(per>=25 & per<45):
    print("C")
elif(per>=45 & per<65):
    print("B")
elif(per>=65 & per<85):
    print("A")
elif(per>=85):
    print("A+")