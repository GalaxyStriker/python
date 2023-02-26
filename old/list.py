copii = ["Gabriel", "Stefan", "Afrodita"] # lista

def main():
    a = raspuns()
    if a == "nu":
        explicit()
    elif a == "da":
        for copil in copii:
            print(copil)

def raspuns():
    while True:
        answer = str(input("Vrei sa ii arat pe toti copii din familie? "))
        if answer == "nu" or answer == "da":
            return answer
            break

def explicit():
    while True:
        nr = int(input("Pe al catalea din lista vrei sa il arat? (in numar de la 1 la 3) "))
        if 0 < nr < 4:
            print(copii[nr - 1])
            break

main()