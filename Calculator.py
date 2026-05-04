# Smart Calculator with History 
history = []

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b==0:
        return "Error!Division by zero not possible"
    return a / b

def power(a,b):
    return a ** b

def modulus(a,b):
    return a % b

while True:
    print("\n Smart Calculator \n")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Power(exponential)")
    print("6.Modulus")
    print("7.Show History")
    print("8.Exit")

 #Take choice
    try:
        choice=int(input("Enter your choice: "))
    except:
        print("Invalid Input!Enter number only(1-8)")
        continue

    #Show history
    if choice==7:
        print("\n Calculation History : ")
        if len(history)==0:
            print("No Calculations yet.")
        else:
            for item in history:
                print(item)
        continue

    #Exit 
    elif choice==8:
        print("Exiting..bye")
        break

    #Take Numbers
    try:
       num1=float(input("Enter First Number :"))
       num2=float(input("Enter Second Number :"))
    except:
       print("Invalid Input!Please enter numbers")
       continue

    #Operations
    if choice==1:
       result=add(num1,num2)
       operation=f"{num1}+{num2}={result}"
    elif choice==2:
       result=subtract(num1,num2)
       operation=f"{num1}-{num2}={result}"
    elif choice==3:
       result=multiply(num1,num2)
       operation=f"{num1}*{num2}={result}"
    elif choice==4:
       result=divide(num1,num2)
       operation=f"{num1}/{num2}={result}"
    elif choice==5:
       result=power(num1,num2)
       operation=f"{num1}^{num2}={result}"
    elif choice==6:
       result=modulus(num1,num2)
       operation=f"{num1}%{num2}={result}"
    else:
       print("Invalid choice! choose between (1-8):")
       continue
    
    #Print Result 
    print("Result:", result)

    #Save History
    history.append(operation)
    