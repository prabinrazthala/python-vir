# if 3>4 or 5>4:
#     print(True)
# elif 3>4 and 5<4:
#     print("test")
# else:
#     print("yo")

a = int(input("enter your percentage"))
if(a>=80 and a<=100):
    print("disctintion")
elif(a<=80 and a>=60):
    print("first division")
elif(a<=60 and a>=50):
    print("second division")
elif(a>=100 or a<=0):
    print("invalid input")
else:
    print("you are fail")




