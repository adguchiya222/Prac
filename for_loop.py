# name = "adnan";


# for i in name:
#     print(i);
#     if(i == "n"):
#         print("N is match in condiftion and you can ignore this line");
        
        
        
        
# colors = ["red" , "blue" , "green" , "pink" , "yellow" , "orange"];

# for color in colors:
#     for sep in color:
#         print(sep)
#     print(color );
#     print("  ");



# for num in range(3 , 13 , 4):
#     print(num )
    


# for num in range(21):
#     if(num / 2):
#         print("The Num is a Even Number")
#     else:
#         print("The Number is ODD Number")    


even_numbers = []
odd_numbers = []

for num in range(1, 21):  # Start from 1 to 20
    if num % 2 == 0:  # Check if the number is even
        even_numbers.append(num)  # Add to even_numbers list
        print(f"{num} is an Even Number")
    else:
        odd_numbers.append(num)  # Add to odd_numbers list
        print(f"{num} is an Odd Number")

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
