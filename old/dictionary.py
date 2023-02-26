copii = {"Gabriel": 10, "Stefan": 13, "Afrodita": 6} # dictionar
copii_keys = list(copii.keys())
copii_values = list(copii.values())

def main():
    a = raspuns()
    if a == "nu":
        explicit()
    elif a == "da":
        for copil in copii:
            print(f"{copil} {copii[copil]} ani")

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
            print(f"{copii_keys[nr - 1]} {copii_values[nr - 1]} ani")
            break

main()