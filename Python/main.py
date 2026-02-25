# print("namaste suyash your are learning python")
"""hello suyash u are learning python"""

# a=12
# print(type(a))

"""# number  -> int
# decimal,fraction -> float
# complex
# v=34j
# print(type(v)) 
"""

"""# String
st ="fkdbj34t6"
print(type(st)) 
"""

"""# Boolean
t=True
f=False
"""


# String
# -----------------------
# a="A"
# print(ord(a)) //65

# b=65
# print(chr(b)) //A

# a ="shar"
# print(a[1])
# print(a[-1],a[3])
# -------------------------


# String Slicing
# ---------------
# a="sher coder"
# print(a[0:4:1])
# print(a[5:10:1])
# print(a[5::1])
# print(a[::])


# type conversion-->int(),float(),str(),bool()
# --------------------------------------------
# a=12
# a=str(a)
# print(type(a))
# print(a)

# a="12"
# a=int(a)
# print(type(a))
# print(a)

# a = 0
# print(bool(a))
# b=123
# print(bool(b))

# falsey->0,0.0,"",[],(),{}

# implicit ,explicit type conversion
# explicit
# print(12/3)

# ------------------------------

# output
# -----------
# name = "Suyash"
# age = "23"
# print("hello my name is ",name,"and my age is",age)
# print(f"my name is {name} and my age is {age}")

# input
# ------------------
# default-/>String
# age = int(input("hello what is your age"))
# print(age)

# a=5
# b=20
# print(b/a)
# print(b//a)
# print(5**2)
# # mode
# print(32%5)


# loop
# print("hello world")

# for loop
# range()-> accept number

# a = range(1,21,1)
# for i in a:
#     print(i)

# for i in range(1,21,1):
#     print(i)


# by default range(0,x,1)
# for i in range(21):
#     print(i)


# for i in range(20,51,1):
#     print(i)

# for i in range(16,0,-1):
#     print(i)

# for i in range(-5,-16,-1):
#     print(i)


# lets print a table of 5

# for i in range(5,51,5):
#     print(i)

# n = int(input("which table you want  ? "))
# for i in range(n,(n*10)+1,n):
#     print(i)

# loops for String (len())
# -----------------------
# (len())

# 1.)using index

# a = "suyash"
# for i in range(0,6,1):
#     print(a[i])

# a = "suyash learn python"
# for i in range(0,len(a),1):
#     print(a[i])


# 2.)using directly on string
# a = "suyash is cool"
# for i in a:
#     print(i)


# for i in range(1,21):
#     if i == 15:
#         break
#     else:
#         print(i)


# for i in range(1,21):
#     if i == 15:
#         continue
#     else:
#         print(i)

# for loop question

# n = int(input("please tell your number"))

# for i in range(n):
#     print("hello world")

# n = int(input("please tell your number"))
# for i in range(1,n+1):
#     print(i)

# n = int(input("please tell your number"))
# for i in range(n,0,-1):
#     print(i)

# n = int(input("please tell your number"))
# for i in range(1,11):
#     print(f"{n} * {i} = {n * i}")


# n = int(input("please tell your number"))
# sum = 0
# for i in range(1,n+1):
#     sum += i

# print(f"your sum is {sum}")


# factorial for number 
# n = int(input("please tell your number"))
# fact = 1
# for i in range(1,n+1):
#     fact *= i

# print(f"your sum is {fact}")

 

# n = int(input("please tell your number:-"))

# for i in range(1,n+1):
#     if i%2 == 0:
#         print(i)


# n = int(input("tell your number : -"))
# even = 0
# odd = 0

# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i    

# print(f"your even and odd sum are {even} , {odd}")     


# n = int(input("which number factors you want: -"))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)


# n = int(input("check your number is perfect or not: -"))

# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i

# if sum ==n:
#     print("your number is perfect")
# else:
#     print("not a perfect number")


# n = int(input("check your number is prime or not: -"))

# count = 0

# for i in range(1,n+1):
#     if n%i == 0:
#         count = count +1
# if count==2:
#     print("your number is prime")
# else:
#     print("your number is not prime")            


# a = "suyash"
# b=""
# # print(a[::-1])
# for i in range(len(a)-1,-1,-1):
#     # print(a[i])
#     b=b+a[i]
# print(b)    



# a = "naman"
# b=""
# # print(a[::-1])
# for i in range(len(a)-1,-1,-1):
#     # print(a[i])
#     b=b+a[i]
# if b == a:
#     print("your String is palindrome")  
# else:
#      print("its not a palindrome")   


# a ="sdfsogn1234@#$%^$&U"

# char = 0
# dig =0
# spchr = 0

# for i in a:
#     if i.isdigit():
#         dig +=1
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr +=1    

# print(f"your digits are {dig}\nyour alphabets are {char}\nyour special character are {spchr}")


# while loop

# a=1
# while a<=30:
#     print(a)
#     a = a+1


# a=int(input("tell your number"))
# while a>0:
#     print(a%10)
#     a=a//10

# a=int(input("tell your number"))
# rev = 0
# while a>0:
#     rev = rev * 10 + a%10
#     a = a//10
# print(rev)   



# a=int(input("tell your number"))
# copy=a
# rev = 0

# while a>0:
#     rev = rev * 10 + a%10
#     a = a//10

# if copy == rev:
#     print("palindromic number")
# else:
#     print("not a palindromic number")  


# random number gussing
# import random
# num = random.randint(1,10)

# tries = 0

# while True:
#     guess = int(input("please guess your number between 1 and 10 :-"))
#     if num == guess:
#         tries +=1
#         print(f"you are right you guessed the number is {tries} tries")
#         break
#     elif num<guess:
#         tries +=1
#         print("go a little lower")   
#     elif num > guess:
#         tries +=1
#         print("go little higher")    
#     else:
#         tries +=1
#         print("sorry u are wrong")    


# Function in python
# --------------------
# print()

# def hello():
#     print("this is a hello function so I am doing hello")
# hello()

# def sum(a,b):
#     print(f"the sum of your number is {a+b}")
# sum(12,12)


# def hello(name ,age):
#     print(f"your name is {name} and your age is {age}")

# # hello("akarsh",22) 
# hello(age = 22, name = "akarsh")   


# def sum(a,b=45):
#     print(f"the sum of your number is {a+b}")
# sum(12)
# sum(12,34)

# def palindrome(st):
#     rev = ""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]

#     if rev == st:
#         print(f"{st} is a palindrome")
#     else:
#         print(f"{st} is not a palindrome")        
# palindrome("naman")
# palindrome("suyash")

 
# Data Structure 

# 1.List-> mutable,duplicate,ordered,hetrogenious
# -------------------------------------------------
# a= [12,13,14,15,16,True,print()]
# print(a[0])
# print(a[0:5])
# print(a[::])
# print(a[-1])
# print(a[-2])

# list traversing and method
#1st way using index
# a= [12,13,14,15,16,34.5]
# for i in range(len(a)):
#     print(a[i])

# # 2nd way directly on values
# for i in a:
#     print(i)     


# methods of list
# print(dir(list))
# help(list)
# l=[1,2,3,4,5]
# l.append(6)
# l.append(7)
# print(l)

# l=[1,3,4,5]
# l.insert(1,2)
# print(l)

# l=[1,2,3,2,4,5]
# l.remove(2)
# print(l)

# Question
# print positive and negative element 
# l=[-45,67,12,-68,-69,34]

# for i in l:
#     if i >=0:
#         print(i)

# for i in l:
#     if i<0:
#         print(i)

# mean of the list
# l=[12,435,67,89,23,25,69]
# sum = 0
# for i in l:
#     sum =sum + i
# print(sum/len(l))


# Greatest element in the list
# l=[12,36,14,19,128,6,13]

# largest = l[0]
# index = 0
# for i in range(len(l)):
#     if l[i]>largest:
#         largest=l[i]
#         index = i

# print(f"your largest number is {largest} at index {index}")

# 2nd Greatest element in the list
# l = [12,16,13,19,17]
# largest = l[0]
# sec_largest= l[0]

# for i in l:
#     if i >largest:
#         sec_largest = largest
#         largest = i
#     elif i>sec_largest:
#         sec_largest = i    
# print(sec_largest,largest)

# list is sorted or not

# l=[12,13,17,14,15]
# for i in range(len(l)-1):
#     if l[i] < l[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted") 


#2. tuple->immutable, duplicates, ordered, heterogenous
# --------------

# a=(1,2,3,4,5,5,5,5,print(),"hello")
# print(type(a))

# index =a.index(5)
# print(index)

# count = a.count(5)
# print(count)

# tuple unpacking
# a,b,c,d=(1,2,3,4)
# print(a,b,c,d)


# 3. set->mutable,not duplicates(unique),unordered heterogenous(string,number,tuples but not everything)
# --------------------------------------------------------------------------------------------------------
# hash value changes every time


# b=hash("hello")
# print(b)

# c=hash((1,8,9,2,3,4))
# print(c)

# a = {1,2,8,9,"hello",3,4,5}
# for i in a:
#     print(i)

# set methods
# a = {1,2,8,9,"hello",3,4,5}
# a.remove(2)
# print(a)

# a.add("suyash")
# print(a)
# a.pop()
# print(a)

# a={1,2,3}
# b={3,4,5}

# # union_set=a.union(b)
# union_set=a|b
# print(union_set)

# # intersection_set = a.intersection(b)
# intersection_set = a&b
# print(intersection_set)

# # difference_set = a.difference(b)
# # difference_set = b.difference(a)
# difference_set = b-a
# print(difference_set)


# symmetric_difference_set = a.symmetric_difference(b)
# symmetric_difference_set = a^b
# print(symmetric_difference_set)


# a={1,2,3}
# b={3,4,5}

# b -= a
# print(b)


# Dictionary->semi-mutable,duplicate,order,heterogeneous
# ------------------------------------------------

# d={1:"hello",2:56}
# print(type(d))

# d={10:100,20:200,30:300,40:400}
# print(d[10])
# print(d[40])
# d[10] = 1000 #updating
# print(d)
# d.update({50:500})
# print(d)
# d[50]=500 # creating
# del d[30] # deleting            
# print(d)

# d={10:100,20:200,30:300,40:400}
# # for i in d:
# #     print(d[i])
# for i in d.values():
#     print(i)

# methods

# help(dict)
# d.clear()
# d2 = d.copy
# print(d.items())



# d1 = {10:100,20:200,30:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)


# d1 = {10:100,20:200,30:300}
# sum = 0

# for i in d1:
#     sum = sum + d1[i]

# print(sum)


# a=[1,1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,1,6,6,6]
# # dict ={1:6,2:3,3:3,4:3,5:2,6:3}
# d={}

# for i in a:
#     if i in d.keys():
#         d[i] +=1
#     else:
#         d[i] = 1

# print(d)

# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     if i in d1.keys():
#         d1[i] +=d2[i]
#     else:
#         d1[i] = d2[i]    

# exception handling
# --------------------------

# a = int(input("tell your number : -"))
# try:
#     print(10/a)

# except ZeroDivisionError:
#     print("sorry you cannot divide by 0")

# print("ok i have done the division")


# a = int(input("tell your number : -"))
# try:
#     print(10/a)

# except Exception as err:
#     print("sorry there ia an err as {err}")

# else:
#     print("good there is no exception") 

# finally:
#     print("i will run no matter what")

# print("ok i have done the division")


# age = int(input("tell your age:-"))
# try:
#     if age < 10 or age > 18 :
#         raise ValueError("your age must be between 10 and 18")
#     else:
#         print("welcome to the club")
# except Exception as err:
#     print(f"an error occured as {err}")        

# print("the lub will start soon ")     


# file handling
# p=open(r'main.py')
# print(p.read())

# r=open("superman.txt",'a')

# r.write("this suyash")
# r.close()






















  



