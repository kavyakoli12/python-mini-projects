num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
choice=input(" + , - , * , / : ")
if(choice== "+"):
    print("Addison :",num1+num2)
elif(choice=="-"):
    print("Subtraction :",num1-num2)
elif(choice=="*"):
    print("Multiplication :",num1*num2)
elif(choice=="/"):
    if(num2 != 0):
        print("Division :",num1/num2)
    else:
        print("Number cannot be zero")
else:
    print("Enter a valid choice")               