# a=10
# b,c=20,30
# d=e=f=40
# print(a)
# print(c)
# print(f)

# a=eval(input("Enter a value"))
# b=eval(input("Enter b value"))
# print(a)
# print(b)
# d,e,f=map(int,input("Enter d,e,f").split())
# print(e)

# age=18
# if age>18:
#     print("Eligible")
# elif age == 18:
#     print("Welcome new voter")
# else:
#     print("Not eligible")
# print("if condition execution")

# no=int(input("Enter no to check"))
# if no%10==7 or no/10==7:
#     print("lucky no")
# else:
#     print("not lucky")

# for i in range(10,100):
#     if i%10==7 or i//10==7:
#         print(i,end=" ")

#comprehensiv list
# list1=[10,20,True]
# print(sum(list1))

# list1=[10,20,False]
# print(sum(list1))

n=10
list1=[]
for i in range(n):
    if i%2==0:
        list1.append(i)
print(list1)
#comprehensive list=> used dealing with huge data
list2=[x for x in range(n) if x%2==1]
print(list2)