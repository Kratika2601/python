#functions
'''def gmean(a,b):
    mean=(a*b)/(a+b)
    print("mean= ",mean)
gmean(8,9)
gmean(8,7)

def greater(c,d):
    if c>d:
        print(c," is greater")
    else:
        print(d," is greater")
greater(26,14)'''

#function arguments

#default argument
def average(a=9,b=1):
    print("the average is: ",(a+b)/2)
average()
average(7,5)
average(4)
average(b=9)

#keyword argument
average(b=9,a=21)

#required argument
def name(fname,mname,lname="agarwal"):
    print("hello", fname,mname,lname)
'''name("kratika") gives an error of
name() missing 1 required positional argument:"mname"'''
name("dinesh","chand")

#variable length argument
def avg(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("average is: ",sum/len(numbers))
avg(5,6,7,1)

def know(**know):
    print(type(know))
    print("hello" , know["first"],know["mid"],know["last"])
know(first="siya",mid="singh",last="rathore")    


