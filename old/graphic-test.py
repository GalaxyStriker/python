# get, return int
def gr_int(prompt):
    while True:
        try:
            y = int(input(prompt))
            return y
        except ValueError:
            print("Acesta nu este un numar intreg. Va rog sa scrieti un numar intreg data viitoare.")

def print_square(size):
    # upper space
    print()
    # for each column in square
    for _ in range(size):
        # Print each brick
        print("#" * round(size * 1.8))
    # lower space
    print()

# print a square
n = gr_int("Da-ti o marime patratului (de la 1 la 50) ")
print_square(n)