import time
t=int(time.strftime("%H"))
if 0<=t<12:
    print("good morning")
elif 12<=t<17:
    print("good afternoon")
else:
    print("good evening")
