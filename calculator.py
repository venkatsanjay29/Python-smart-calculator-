def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b
    
def div(a,b):
    if b==0:
        print("Error! Cannot divide by zero")
    return a/b

print("*"*35)
print("      SMART PYTHON CALCULATOR      ")
print("*"*35)

while True:
    print("\nChoose an operation: ")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    
    c=int(input("Enter your choice (1-5): "))
    
    if c==5:
        print("\nThank you for choosing smart calculator")
        break
    if c not in [1,2,3,4,5]:
        print("Invalid choice! Please try again")
        continue
    try:
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: ")) 
    except ValueError:
        print("Please enter valid numbers")
        continue
        
    if c==1:
        r=add(num1,num2)
        s="+"
    elif c==2:
        r=sub(num1,num2)
        s="-"
    elif c==3:
        r=mul(num1,num2)
        s="*"
    elif c==4:
        r=div(num1,num2) 
        s="/"
    
    print(f"\nResult: {num1} {s} {num2} = {r}")   