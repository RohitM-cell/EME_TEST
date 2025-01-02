# Program to accept tw o numbers and perform the calulator task 

print("Calculator")
print("Choose your Options: 1.Addition ,2.Substraction ,3.Multiplication ,4.Division")

choice=int(input("Enter your Choice : "))

if choice==1:
    num1=int(input("Enter Number 1: "))
    num2=int(input("Enter Number 2: "))
    print("Addition: ",num1+num2)
elif choice==2:
    num1=int(input("Enter Number 1: "))
    num2=int(input("Enter Number 2: "))
    print("Substraction: ",num1-num2)
elif choice==3:
    num1=int(input("Enter Number 1: "))
    num2=int(input("Enter Number 2: "))
    print("Multiplication: ",num1*num2)
elif choice==4:
    num1=int(input("Enter Number 1: "))
    num2=int(input("Enter Number 2: "))
    print("Division: ",num1/num2)
else:
    print("Invalid Output")
