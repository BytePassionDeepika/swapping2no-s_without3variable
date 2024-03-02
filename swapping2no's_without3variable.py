num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
print(f"Before Swapping: num1={num1} num2={num2}")
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(f"After Swapping: num1={num1} num2={num2}")