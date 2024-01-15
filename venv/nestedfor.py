# for a in range(1,11,1):
#     for i in range(1,11,1):
#         multiply = a * i
#         print(f'{a} X {i} = {multiply}')

# a = [1,3,5,6,9]
# for items in a:
#     for x in range(1,11,1):
#         print(f'{items} X {x} = {items * x}')


user_input = int(input("enter a number for multiplication"))
if(user_input < 5):
    for items in range(1,user_input + 1,1):
        multi_data =int(input("enter a number==>"))
        for i in range(1,11,1):
            print(f'{multi_data} X {i} = {multi_data * i}')
else:
    print("for loop ended")













