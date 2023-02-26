#Define the main program, because this way you will get a better understanding of the steps of your code.

def main():
    nume = input("Care este numele tau? ").strip().title()
    repetari = ia_nr_de_repetari()
    if nume:
        greet(nume, repetari)
    else:
        greet("", repetari)

def ia_nr_de_repetari():
    while True:
        repetari = int(input("De cate ori sa iti repet numele? "))
        if repetari > 0:
            return repetari
            break
        
        """ metoda mea originala
        if repetari <= 0:
            repetari = int(input("De cate ori sa iti repet numele? "))
        else:
            break
        """


#Define function and give parameter "cui" with the word "lume" as default. You can pass any word to define the variable "cui"
def greet(cui="lume", loops=1):
    for _ in range(loops):
        print (f"Salut, {cui}!")

main()