## Program to check if the number is divisible by 2 or not

number=int(input("Enter a number:"))
if number ==0 or number ==1:
    print("Enter other number")
elif number > 2:
            if(number % 2 ==0):
                print("Divisible by 2")
            else:
                print("Not divisible by 2")
                