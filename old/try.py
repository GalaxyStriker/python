def main():
    y = gr_int("De cate ori?")
    if y != "stop":
        print(f"y is {y}")

def stop():
    print_line()
    print("OK, I'll stop, Jesus.")
    print_line()

def print_line(length=22):
    print("-" * length)

# get, return int
def gr_int(question):
    while True:
        try:
            y = input(question)
            if y == "stop":
                stop()
                return y
            y = int(y)
        except ValueError:
            print_line(19)
            print("Numarul acesta nu e un numar natural. Va rog sa scrieti un numar natural.")
            print_line(19)
        else:
            return y

main()