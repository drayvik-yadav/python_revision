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












float0=5.0
print(type(float0))
float1=float(5)#if i'm write only 5 then id() is different but when i write 5. then varivale id() is same 
float2=5.00
float3=5.0000
print(float0,id(float0))
print(float1,id(float1))
print(float2,id(float2))
print(float3,id(float3))
float4=10/5
float5=4/2
print(float4,id(float4))
print(float5,id(float5))

#yoep same value flot id() is same also 5.,5.0,5.00,5.000 are equal and also varible id is also same




#garbase collaction
status="active"
status="close"

#here reassign varible 
#so here active in avaivale in memory but not labeled by any varible sor it delated by automatically python it's called garbase collaction




x=[10,20,30]
y=x
x.append(40)
print(y) #[10,20,30,40] how? 

x1=10
y1=x1
x1=5
print(y1) #10 how? because int is immutable so when i reassign x1=5 then it create new memory location for 5 and x1 point to that but y1 still point to 10



