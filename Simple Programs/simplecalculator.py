def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print("CALCULATOR")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice=int(input("Enter your choice(1/2/3/4):"))

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

if choice==1:
    print("Sum is",add(num1,num2))

if choice ==2:
    print("Difference is",subtract(num1,num2))
    
if choice==3:
    print("Product is",multiply(num1,num2))
    
if choice==4:
    print("Division is",divide(num1,num2))
    
