if __name__ == '__main__':

    annee=int(input("Veuillez entrer l'anée :"))

    while annee<=0:
        annee=int(input("Saisissez une année positive :"))

    try:
        if((annee%4==0 and annee%100!=0) or (annee%400==0)):
            print("L'anee antrée est bixectille.")
        else:
            print("L'anée n'est pas bixectille")

    except:
        print("Erreur ! L'année incorecte.")


mot="Institut de Formation et de Recherche en Informatique"


for i in mot:
    if i in "azertyiopjgdvdffbdgs":
            print(i)
    else:
            print("-")
