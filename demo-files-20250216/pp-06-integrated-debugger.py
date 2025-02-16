# p. 15
# demo of the debugger
def func_1():
    print("In function 1.")

def func_2():
    name = input("What's your name? ")
    return name

print("Welcome to the debugger demo!\n")

print("This will show us how the debugger steps through, and into, code.")

func_1()

name = func_2()
print(f"Hello, {name}")

print("Bye")