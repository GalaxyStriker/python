def gr_int(prompt):
    while True:
            try:
                y = float(input(prompt))
                return y
            except ValueError:
                print("Acesta nu este un numar zecimal. Va rog sa scrieti un numar zecimal data viitoare.")