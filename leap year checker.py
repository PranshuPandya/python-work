print('Hello!,Welcome to leap year checker.')
print('Enter the year of which you want to ckeck')
year=int (input())
if (year%400==0) :
    print(year,' is leap year.')
elif (year%100!=0) and (year%4==0):
    print(year,' is leap year.')
else:
    print(year,' is not a leap year.')    