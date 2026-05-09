'''#1st que
num=int(input("enter a number:"))
if num>0:
    print("the number is positive",num)
else:
    print("the number is not positive")

#2 que
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=b**2-4*a*c
import math
if d>0:
    print("real roots exist")
    x1=(-b+ math.sqrt(d))/2**a
    x2=(-b - math.sqrt(d))/2**a
    print("roots are:",x1,x2)
elif d==0:
    print("one root")
    x=-b/2*a
    print("root is",x)
else:
    print("no real roots exist")


#3que
n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
n3=int(input("enter n3:"))
if n1>n2 and n1>n3:
    print(n1,"is greater")
elif n2>n1 and n2>n3:
    print(n2,"is greater")
else:
    print(n3,"is greater")

#4th que
n=int(input("enter a number:"))
if n== 0:
    print(n,"is zero")
elif n>0:
    print(n,"is greater than zero and it is positive")
else:
    print(n,"is not greater then zero and it is negative")
if abs(n)<1:
    print("small")
elif abs(n)>100000:
    print("large")
else:
    print("medium")

#5th que
choice=int(input("enter your choice:"))
if choice==1:
    print("Monday")
elif choice==2:
    print("Tuesday")
elif choice==3:
    print("Wednesday")
elif choice==4:
    print("Thursday")
elif choice==5:
    print("Friday")
elif choice==6:
    print("Saturday")
elif choice==7:
    print("Sunday")
else:
    print("invalid choice brooooooooooooo!!")


#6th qu
num=1
for i in range(1,11):
    for j in range(1,i+1):
        print(num,end="")
        num=num+1
    print()

#7th que
for i in range(1,7):
    for j in range(6-i):
        print(" ",end="")
    for j in range(i):
        print(i,end=" ")
    print()

#8th que
num=1
for i in range(1,6):
    for j in range(1,i+1):
        print(num,end="")
        num=num+1
    print()


#9th que
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#10th que
for i in range(1,11):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#11que
n=int(input("enter n:"))
sum=0
for i in range(n):
    o=int(input("enter odd numbers:"))
    if o%2!=0:
        sum=sum+o
print("sum of odd numbers is:",sum)

#12que
num=int(input("enter number:"))
for i in range(1,11):
    print(num,"X",i,"=",num*i)

#13 ques
num=4
for i in range(num):
    print("num is", i, "its cube is",i**3)



#14 ques
n=int(input("enter n:"))
sum=0
for i in range(n):
    num=int(input("enter n numbers:"))
    sum=sum+num
    avg=sum/n
print(sum)
print(avg)

#15que
for i in range(1,11):
    print(i)


#16 que
year=int(input("enter year to check leap year:"))
if year%400==0:
    print(f"{year} is leap year")
elif year%100==0:
    print(f"{year} is not a leap year")
elif year%4==0:
    print(f"{year} is a leap year")
else:
    print(f"its not leap year broo")

#17que
letter=input("enter letter:")
if letter in "aeiouAEIOU":
    print("its a vowel")
else:
    print("its a consonant")

 '''
#18que
