def main():
    x = int(input("Da o valoare lui x: "))
    if parity(x):
        print("x e par")
    else:
        print ("x e impar")

#parity -- check if number is even or odd. % (modulo) determines the rest of the division. (Ex: 3/2 = 1, remainder 1; 2/2 = 1, remainder 0. )
def parity(n):
    return n % 2 == 0

main()