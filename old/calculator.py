from math import sqrt
from int_input import gr_int

def main():
    a = gr_int("Type your digit here:  ")
    print("")
    print(f"{a} + {a} = {sum(a,a)}", end="\n\n")
    print(f"{a} squared is {square(a)}", end="\n\n")
    print(f"Square root of {a} is {sqrt(a)}", end="\n\n")
    print(f"{a} rounded is {round(a)}", end="\n\n")

def sum(a,b):
    return a + b

def square(n):
    # ** means to the power of
    return round(n ** 2, 2)

main()
