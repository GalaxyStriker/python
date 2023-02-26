a = float(input("What's a? "))
b = float(input("What's b? "))

# Using only ifs will still run them, even if the previous if was true. The elif statement
# runs only if the previous statement returned false.

if a > b:
    print(f"a is bigger than b, because {a} > {b}")
elif a < b:
    print(f"a is smaller than b, because {a} < {b}")
else:
    print("a is equal to b")