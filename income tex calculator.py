print('Hello!,Welcome to Income Tex Calculator')
print('Enter your income')
income=float (input())
if income<=40000:
    print("You don't have to pay any income tex as your income is below 40,000.")
else :
    print('Your income tex is of Rs.',(0.15)*(income-40000))    
