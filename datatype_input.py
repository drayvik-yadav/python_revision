#primtive data type in python
#integer

n=45
n1=-45
n2=0
print(n,type(n))
print(n1,type(n1))
print(n2,type(n2))

f=5.0
f1=5.
f2=0.00
print(f,type(f))
print(f1,type(f1))
print(f2,type(f2))


#Bolean
x=True
y=False
x1="True"
print(x,type(x))
print(y,type(y))
print(x1,type(x1))

#String
s="Hello"
s1='Hello'
s2='''Hello'''
s3="""Hello"""
s4='hi, I\'m Abhishek'
print(s,type(s))
print(s1,type(s1))  
print(s2,type(s2))
print(s3,type(s3))
print(s4,type(s4))

#None data type (none)
not_data=None
print(not_data,type(not_data)) 
#None is a special data type in python it represent the absence of value or null value it is used to indicate that a variable does not have any value assigned to it yet or to indicate that a function does not return any value. It is also used as a default value for function arguments when no value is provided. None is a singleton object in python, which means that there is only one instance of None in the entire program and it can be accessed using the None keyword.


#type casting
#beetween int and float
#Implicit conversion (outomatic by python)
a=5
b=2.5
c=a+b
print(c,type(c))

#Explicit conversion (manully by function like int() float() str())
c=int(c)
print(c,type(c))
print(float(c))#7.0 here data lose

#string to int or float 
#possible 
s=str(c)
print(s,type(s))
s=int(s)
print(s,type(s))

#not possible
s="abhi"
# n=int(s) #ValueError: invalid literal for int() with base 10: 'abhi'


#boolean
print(bool(s)) #True because here bool work str is empty or not
print(bool(""))#False becUSE  str empty

print(bool(0))#f
print(bool(1))#t
print(bool(3))#t
print(bool(4))#T
print(bool(5))#t