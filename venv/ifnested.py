# a = "test"
# b = "test"
# print(a)

# if a==b:
#     print("pass")

# if a>b:
#     print("test pass")
# elif (a==b):
#     print("eaual pass")
#     if isinstance(123,int):
#         print("datatype pass")
#     elif(a<b):
#         print("opeartor pass")
# else:
#     print("whole program fail")

# one line if condition
# gender = "m"
# data = "Male" if gender == "m" else "Female"
# print(data)

#pseudo code
#input total sales -> type casting also at int
#threshold sales = target sales
#1 input total sales
#2 threshold sales = 3000
#3 3000-4000 3% commision
#4 4000-5000 5% commission
#5 5000 - upto 10% commission
#6 no commision
total_sales = int(input("enter your sales"))
threshold_sales = 3000
if(total_sales >= threshold_sales):
    if (total_sales >= 3000 and total_sales <= 4000):
        print("commision percentage is 3%")
    elif(total_sales >= 4000 and total_sales <= 5000):
        print("commision percentage is 5%")
    elif(total_sales >= 5000):
        print("commision percentage is 10%")
    else:
        print("no commission")
else:
    print(f'Sorry you didnnot meet your target')


