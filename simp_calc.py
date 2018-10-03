#program for simple calculator

i=int(input("Enter value of i: "))
j=int(input("Enter value of j: "))
o=input("what do you want to do? +,-,x,/: ")

def add(a,b):
	return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def divide(a,b):
    return a/b

if(o=='+'):
    print("addition=",add(i,j))
elif(o=='-'):
    print("subtraction=",sub(i,j))
elif(o=='x'):
    res=mult(i,j)
    print("multiplication=",res)
elif(o=='/'):
    print("division=",divide(i,j))