# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lvusb5Nz27cXCm1SpBRq77PviFJaIA2z
"""





"""**class1**

"""

# single line comment
''' double line comment
excuse me'''
# num_1,_mum,123num.
_num_1='chetan'
print(_num_1)

c1= 56
c2=54
print(c1+c2,type(c1),type(c2))

f1=34
f2=67.8
print(f1+f2,type(f1+f2))

#concatenating meaning combining two  data
f1=678
f2=78
f3=f1*f2
print("mulplication of two numbers",f3,"\n   right")

myList=[1,2,'data',"structures"]
myList[-4]=3
print(myList)
# list is a collection data type which is mutable

num1=True

num2= False
print(2>5)

num1=10
num2='10'
print(num1+int(num2))

c1=float(input("the value of number:"))
c2=float(input("the value of number:"))
print(c1+c2)



"""**class2**"""

#list- mutable collection datatype
mylist=[1,2,3,4,5]
#update
mylist[0]=0
mylist[1]=1
print(mylist)
#append
mylist.append(6)
print("after appending mylist",mylist)
#insert
mylist.insert(2,2)
print("after inserting",mylist)
#remove ->removes the first occurence of the value in ()
mylist.append(0)
mylist.remove(0)
print(mylist)
#pop removes the specified index element
mylist.insert(0,0)
mylist.pop(-1)
print(mylist)
#extend 
mylist1=[7,8,9,10]
mylist.extend(mylist1)
print(mylist)
#inserting list in between lists
mylist.insert(5,mylist1)
print(mylist)
del mylist
mylist1=[7,8,9,10]
mylist.extend(mylist1)
print(mylist)

#mytuple ordered collection of datatypes, immutable,()
mytuple=(1,2,'speak',23.4)

print(mytuple[2])
mytuple.insert()

myli=[1,3,2]
four=int(input("the value is:"))
myli.insert(2,four)
print(myli)

#dictionary datatype symbol{},mutable
mydic={
    "username":"chetan",
    "password":"balumamma123",
    "age":19
}
print(mydic)
mydic["username"]=123
mydic['age']="nineteen"
print(mydic['username'],mydic['age'])
mydic["dateofbirth"]=2003
print(mydic["dateofbirth"])

#set unordered collection datatypeimmutable,ccant index and get the value
a={1,2,"chetan"}
a1={3,2,"krishna"}
a2=a.intersection(a1)
print(a2)
a3={True,False,1.2}
print(a1.intersection(a3))
a=frozenset(["chetan",2,5])
print(a)
a2=a&a1&a2
 #| stands for union,& stands for intersection
print(a2)
a1.clear()
print(a1)
def name():
  a=input("Your name is:")
  print("my name is:",a)
  name()

def name():
  a="chetan"
  print("my name is:",a)
  name()

def n():
  name=input("Your name is:")
  print("my name is ",name)
n()

l1=[1,2,3,"chetan"]
#iteration by iter and next method
myiteration =iter(l1)
print(next(myiteration))
print(next(myiteration))
print(next(myiteration))
print(next(myiteration))

#for loop printsnumbers in the list
tuple1=(1,2,3,"chetan")
for i in tuple1:
  print ( "the values of tuple 1 :",i)
for y in range (1,8):
  print( 'the square of number',y,'is',y**2)

def calc():
  for a in range(2):
    for b in range(2):
      a=int(input("the first value:"))
      b=int(input(" the second value:"))
      print(" the sum of first values is",a+b)
calc()

#modules imports data
import math
x=math.pi
print(math.sin(x/2))
import datetime
print(datetime.datetime.now())

#slicing prints ranges of data
a="chetan"
print(a[0:2])
print(a[:4])
print(a[3:])

#files -> three types of mode
#read mode
# write mode
#append mode
myfiles=open("c.txt","r")
print(myfiles.read())





files=open("begining",'r')
print(files.read())

files=open("begining","w")
files.write("my name is chetan \n")
files=open("begining","r")
print(files.read())

files=open("begining","a")
a=input()
files.write(a )
files=open("begining","r")
print(files.read())

f=open("c1.txt","r")
print(f.read())

f=open("c1.txt","w")
f.write("my name is chetan \n")

f=open("c1.txt","w")
f.write("chetan \n")

a=input()

f=open("c1.txt","w")
f.write(a)

mylines=["This is chetan\n","i believe in myself\n","And one day i am going to become bilionaire\n"]
  f=open("c1.txt","w")
  f.writelines(mylines)
  f=open("c1.txt","r")
  print(f.read())

#context manager
with open("c1.txt","w+") as file:
  file.writelines(mylines)
  print(file.read())
with open("c1.txt","a") as files:
  files.write("I will get a beautiful and a loyal wife")
with open("c1.txt","r") as files:
  print(files.read())

a=int(input())
b=int(input())
o=input()
if( o=="+"):
  print(a+b) 
elif(o=="-"):
  print(a-b)
elif(o=='*'):
  print(a*b)
elif(o=="/"):
  print(a/b)

#context manage["\n this is chill doing sex in the six with your ex \n","thank you regards chill \n"]
lines=["This is chill doing sex in the six with your ex \n","Thank you regards chill \n"]

with open("cool.txt","a") as file:
 file.writelines(lines)
with open("cool.txt","r") as file:
 print(file.read())

"""# New Section"""

#STOP WATCH
i=0,
j=0
for i in range(0,61):
    if (i==60):
      j=j+1
      i=0
    with open("cool.txt","w") as file:
     file.write(f"{j}:{i}")
    with open("cool.txt","r") as file: 
      print(file.read())

# % operator
# .format string
# fstring
print(" hello %s\n This is chill with kill\nFuck you %s" %(input("enter your name:"),input("Enter the name:")))

#.format used for specifying indices works exactly like % operator
i=(input())
j=(input())
print("hello {0}\nthis is {1}" .format(i,j) )

# fstring

print(f"this is %s and his rollnumber is {input()}" %(input("your name:")))