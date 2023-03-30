import math
def sum(x,y):
    return (x+y)
def sub(x,y):
    return (x-y)
def mul(x,y):
    return(x*y)
def div(x,y):
    return(x/y)
def power(x,y):
    return(pow(x,y))

print("Welcome to simple caculator")
n=int(input("How much do you want to caculate?"))
for i in range(n):
    a=int(input("Enter a number-> "))
    b=int(input("Enter a number-> "))
    print("Which operation do yo want to do?")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Power")
    print("6.Exit")
    choice=int(input("nter yoyr choice"))
    if(choice==1):
        print(sum(a,b))
    elif(choice==2):
        print(sub(a,b))
    elif(choice==3):
        print(mul(a,b))
    elif(choice==4):
        print(div(a,b))
    elif(choice==5):
        print(power(a,b))
    elif(choice==6):
        print("EXIT")
        break
    else:
        print("Please try again")

