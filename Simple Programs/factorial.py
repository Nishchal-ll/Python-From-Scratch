number=int(input("Enter a number to calculate factorial:"))
def factorial(n): 
    if n==0 or n ==1:
        return 1
    elif n >=2:
        return n*factorial(n-1)
result=factorial(number)
print(result)
            