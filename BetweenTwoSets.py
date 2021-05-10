numbers = [int(n) for n in input().split(" ")]
numbersn = [int(n) for n in input().split(" ")]
numbersm = [int(n) for n in input().split(" ")]
from math import gcd
#a = [100, 200, 150]   #will work for an int array of any length
lcm = numbersn[0]
for i in numbersn[1:]:
  lcm = lcm*i//gcd(lcm, i)
# print(lcm)
num1=numbersm[0] 
num2=numbersm[1] 
gd=gcd(num1,num2)
for i in range(2,len(numbersm)): 
    gd=gcd(gd,numbersm[i]) 
# print(gd)
count=0
if(lcm>gd):
    count=0
elif(lcm==gd):
    count=1
else:
    for i in range(lcm,gd+1):
        if(i%lcm==0 and gd%i==0):
            count+=1
print(count)
# p=input()
# n=int(p.split())
# m=int(input())
# listn=[]
# listm=[]
# for i in range(0,numbers):
#     p=int(input())
#     listn.append(p)
# for i in range(0,m):
#     p=int(input())
#     listm.append(p)
# print(listn)
# print(listm)
# numbersn=numbersn.sort()
# numbersm=numbersm.sort()
