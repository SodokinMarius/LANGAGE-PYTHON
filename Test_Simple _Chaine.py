#coding utf-8
if __name__ == '__main__':

    nom=input("Entrer votre nom : ")
    prenom=input("Votre prenom svp : ")
    age=int(input("Quel âge avez vous ? "))
    Message="Vos Informations Personnelles"
    fin="Merci"+" "+str(nom.capitalize())
    print(Message.upper().center(40))
    print("Vous êtes {0} {1} et vous avez {2} ans ".format(nom,prenom,age))
    print("Votre nom est de {tailNom} caractère et votre" \
          " prenom {tailpre}".format(tailNom=len(nom),tailpre=len(prenom)))
    print(nom[3:])
    print(fin.center(50))
    i=0
    while(i<len(nom)):
        print(f"Caratere {i} : {nom[i].upper()}")
        i+=1


        #help(list)