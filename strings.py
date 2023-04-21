name="kratika"
print("hello, ",name)

#multiline string using triple single or double quotes
para="""heyyy kratika!!
how you doing ?
if everything fine!!?"""
print(para)

#accessing a string
print(name[2])
print(name[5])
#print(name[7])    this throws an error of string index out of range

#looping through a string
for ch in name:
    print(ch)

#string slicing
fruit="mango"
print(fruit[:])
print(fruit[:4])
print(fruit[1:])
nm="harry"
print(nm[-4:-2])

#length of string
print(len(fruit))
