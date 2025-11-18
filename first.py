'''print("hello raj")
name = "raj"
age = 22
prise = 25.999
print ("My name is :",name)
print("my age is :", age)
a = 25698741268
b = 6987423148
diff = a-b
print(diff)
input ("enter your age:")
print (name)

# this is my first comment
light = (input("enter a light color :" ))
if (light == "red" ) :
    print("stop for few sec")
elif (light == "yello"):
    print("go slow")
elif (light == "green"):
    print("dont stop")
else:
    print("go go go signal is brokan")'''



# LIST
"""mark1 = 94.2
mark1 = 85.2
mark1 = 95.2
mark1 = 85.2
mark1 = 57.2

marks = [95.2,85.1,95.1,75.6,65.5]
print (marks)
print (type(marks))
print(marks[0])
print(marks[1])
print(len(marks))
student = [15,45,55,8,69,95]
print(student)
# student[0]="pruthviraj"
print(student)
print(student.sort())
print(student)
"""
"""color1 = (input("enter color1:" ))
color2 = (input("enter color2:" ))
color3 = (input("enter color3:" ))
colors = [color1 , color2, color3]
print(colors)

collection = {1,2,3,4,5}
collection.add(6)
collection.add((1,2,7))
print(collection)
print(type(collection))
collection1= set()
print(type(collection1))

dic = { 
    "cat" : "a small animal",
    "table":["kdnfh jnxbd jddbyfbf","kdkm dkfggf kdnff lfnf"]
    
}

print(dic)

subject = {"python","java","c++","c","javascript","java","python","c","c++"}
print(len(subject))

'''marks = {}
x=input("enter mark pyhon :" )
marks.update({"pyhon " : x })
y=input("enter mark java :" )
z=input("enter mark c++ :" )
marks.update({"java " : y,"c++ " : z})
print(marks)'''


# while loop

A = 1
while (A<=100):
    print(A)
    A += 1

b =100
while(b>=1):
    print(b)
    b -=1

n = int(input("enter any num : " ))
m=1
while(m<=10):
    print(n * m)
    m += 1

g =1
while (g<=10):
    print(g**2)
    g +=1

num =8
sum = 0
c =1
while (c<=num):
    sum += c
    c += 1
print(sum)

f = open("raj.txt","a") 
f.write("i want to write javascript file from today. 12345789789789456123")
f.close()

import os
os.remove("raj.txt")"""

class student:
    name="raj Pawar"

s1 = student()
print(s1.name)

s2 = student()
print(s2.name)



