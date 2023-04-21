#strings are immutable
st1="  !!!Kratika711!!!"
st2="silver spoon"
st3="introduction tO jS"
st4="welcome to the console!!!\n"
#string methods
print(st1.upper())
print(st1.lower())
print(st1.strip())
print(st1.rstrip("!"))
print(st1.replace("Kr","V"))
print(st2.split(" "))
print(st3.capitalize())
print(st3.center(50))
print(len(st3))
print(len(st3.center(50)))
print(st2.count("s"))
print(st1.endswith("!!!"))
print(st4.endswith("to",4,10))
print(st4.find("the"))
print(st4.find("ishhh"))
print(st1.isalnum())
print(st2.isalpha())
print(st4.islower())
print(st4.isupper())
print(st4.isprintable())
print(st2.isspace())              #returns true if str="     "
print(st3.istitle())
print(st3.title())
print(st3.swapcase())
print(st4.index("ishhh"))
