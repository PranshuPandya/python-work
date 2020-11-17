print('Hello!,Welcome.')
print('How many numbers do you want to average?')
no_of_no=int (input())
num=[]
sum=0
for i in range(0,no_of_no):
    print('Enter number ',i+1)
    num.insert(i,float (input()))
    sum=sum + num[i]
print('You have entered following numbers')
print(num)
print('Average of the numbers = ',sum/no_of_no)    
print("Average of the numbers upto two decimal places is = "+"{:.2f}".format(sum/no_of_no))