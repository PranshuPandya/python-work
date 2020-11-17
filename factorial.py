print('Hello!,Welcome.')
print('Enter the number of which you want to find factorial')
number=int (input())
fac=1
for i in range(1,(number+1)):
    fac*=i
print('Factorial of the given number is ',fac)    