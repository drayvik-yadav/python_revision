integer=500
print(integer)
print("type of variable is:",type(integer))
integer1=integer
integer2=500
print(id(integer))
print(id(integer1))
print(id(integer2))
#in output is means memory location is same for all this variable means that proved python use referance for same valve

#now i'm checking this for str 
name="Abhishek"
name1="abhishek"
print(name==name1) #False that prove python case senctive 
name2=name
name3="Abhishek"
name4='abhishek'

#let's first check varivle type:
print(type(name))


#print(id(name,name2,name3,name4)) #error  i thing only one variable take at atime ok...
# now i want to check where i take 2 or more id() function in one print or not
# print(id(name),id(name1)) # youp i can do like that

print(name,id(name))
print(name1,id(name1))
print(name2,id(name2))
print(name3,id(name3))
print(name4,id(name4))
# yes varible id() is same for same str() value

#is it also working for float 
#after many try i can not use float=5.0 why?
#so first check reverse word what is it?

# import keyboard #i'm unable to import this libary this time to i'll do it later 












Float=5.0
print(type(Float))



