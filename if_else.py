# a = int(input("Enter your Age:"))

# print("Your age is:" , a);

# if(a<18  ):
#     print("You are Underage for Driving so please wait for a while");
# elif(a>=60 and  a<70):
#     print("Sir Please you are old so be safe and drive carefully");
# elif(a>70):
#       if(a>70  and a<90):
#          print("Sir you can not dive becaue you are old and you can drive in some emergency cases but please be safe at that time ")
#       else:
#           print("Sir you can not drive you are too old")   
# else:
#     print("Yes you can drive and be a safe driver");


from datetime import datetime

# Get the current hour
current_hour = datetime.now().hour

# Check the time and print the appropriate greeting
if 5 <= current_hour < 12:
    print("Good morning!")
elif 12 <= current_hour < 18:
    print("Good afternoon!")
elif 18 <= current_hour < 22:
    print("Good evening!")
else:
    print("Good night!")
