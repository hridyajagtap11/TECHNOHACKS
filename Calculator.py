def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
def modulus(num1,num2):
    return num1%num2

print("***** Calculator *****")      
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
choice=int(input("Enter your choice:"))
num1=float(input("Enter the value of first number:"))
num2=float(input("Enter the value of second number:"))

if(choice==1):
    print("Addition of two numbers",add(num1,num2))
elif(choice==2):
    print("Subtraction of two numbers",subtract(num1,num2)) 
elif(choice==3):
    print("Multiplication of two numbers",multiply(num1,num2))
elif(choice==4):
    print("Division of two numbers",divide(num1,num2))
elif(choice==5):
    print("Modulus of two numbers is",modulus(num1,num2))   
else:
    print("Invalid Option")                