# Ask for input on the question
zi = input("Ce zi e azi? ").strip().lower()
print()
# Clear spaces inputted by accident and decapitalize the input
# Could be done like: zi = zi.strip().lower()
# For capitalizing the .capitalize method would be used to capitalize the first word or .title to capitalize all the words

# Print the message along with the input given by the user
# Using the F-string method
match zi:
    case "luni":
        print("lucreaza cu pauze")
    case "marti":
        print("nu te da batut")
    case "miercuri":
        print ("esti la jumatatea saptamanii")
    case "joi":
        print("mai poti lucra!")
    case "vineri":
        print("ultimul efort!")
    case "sambata" | "duminica":
        print("azi e zi de odihna, te poti relaxa")
    case _:
        print("verifica daca nu ai comis greseli de tipar")


# Using the no end argument
"""
print("Odihnestete, fiindca azi este ", end="")
print(zi, end="")
print(".")
"""

nr = int(input("Scrie un numar de la 50 la 100: "))

if 90 <= nr:
    print("Numarul are o valoare dintre numerele de la 90 pana la 100")
elif 80 <= nr:
    print("Numarul are o valoare dintre numerele de la 80 pana la 89")
elif 70 <= nr:
    print("Numarul are o valoare dintre numerele de la 70 pana la 79")
elif 60 <= nr:
    print("Numarul are o valoare dintre numerele de la 60 pana la 69")
else:
    print("Numarul are o valoare dintre numerele de la 50 pana la 59")