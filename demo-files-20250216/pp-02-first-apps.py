# p. 8

# variables - string, int, float
number_1 = 5
first_name = "Bob"
success = False

print(f"number_1 = {number_1}")
print(first_name)
print(success)

# comments - use a hashtag

# arithmetic operators: +, -, *, /, %
nbr_1 = 9
nbr_2 = 4

print(f"+ {nbr_1 + nbr_2}")
print(f"- {nbr_1 - nbr_2}")
print(f"* {nbr_1 * nbr_2}")
print(f"/ {nbr_1 / nbr_2}")
print(f"// {nbr_1 // nbr_2}")
print(f"% {nbr_1 % nbr_2}")
print(f"** {nbr_1 ** nbr_2}")
print(f"^ {nbr_1 ^ nbr_2}")

# console interaction: print(""), print(f"")

# escape sequences: \n, \t
message = "This is line one.\nThis is line two.\tAfter the tab.\\"
print(message)

# 'end' attribute: print('a', 'b', 'c', sep="-") => a-b-c
print('a', 'b', 'c', sep="|")

# get user input: input("...") => returns string
name = input("What's your name? ")
int_num_1 = int(input("Enter first #: "))
int_num_2 = int(input("Enter first #: "))
print(int_num_1 + int_num_2)

# convert to int, float => int("..."), float("...")

# p. 9
# if statements: if, elif, else
# note the use of colon to note blocks of code!
light_color = "green"

if light_color == "green":
    print("Go")
elif light_color == "yellow":
    print("Slow Down")
elif light_color == "red":
    print("Stop")
else:
    print("Invalid light color")

# while loop: 
while (True):
    print("in the while loop!")
    response = input("Again? ")
    if response == 'n':
        break
