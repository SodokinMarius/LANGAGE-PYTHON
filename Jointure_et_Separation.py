if __name__ == '__main__':

    try:
        nombre=float(input("Entrer un nombre flottant : "))
    except ValueError:
        print("Le type de valeur ne correspond pas !")
    except ZeroDivisionError:
        print("Ce n'est pas l'opération attendu :")
    except TypeError:
        print("Le paramètre attendu doit être un floattant ")
    else:
        print("Votre nombre : {}".format(nombre))
    maliste=list()

    nombre=str(nombre)
    maliste=nombre.split(".")
    print(maliste)
    part1=maliste[0]
    part2=maliste[1][:3]

    machaine=",".join([part1,part2])
    print("le flottant {} revient à {} : ".format(nombre,machaine))
    print(maliste nombre,machaine)