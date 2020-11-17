print('Hello!,Welcome.')
print('How many numbers do you want enter?(you have to insert atleast 2 numbers)')
non=int (input())
num=[]
for i in range(0,non):
    print('Enter number ',i+1)
    num.insert(i,float (input()))
    if i==0:
        min=num[0]
        max=num[0]
    if num[i]>max:
        max=num[i]
    if num[i]<min:
        min=num[i]
print('You have entered following numbers')
print(num)               
print('Minimum of the numbers = ',min)  
print('Maximum of the numbers = ',max)  
