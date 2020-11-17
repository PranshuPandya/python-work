print('Hello!,Welcome.')
data=[10,12,3,45,67,34,80,56]
print('We have following set of numbers :')
print(data)
even=[]
odd=[]
for i in range(0,8) :
    if data[i]%2==0 :
        f=0
        even.insert(f,data[i])
        f=f+1
    else :
        g=0
        odd.insert(g,data[i])
        g=g+1
print('even numbers from the list are :',even )            
print('odd numbers from the list are :',odd) 