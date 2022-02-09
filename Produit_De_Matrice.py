#coding: utf-8
def saisi_taille():

    try:
        print("Entrer la taille de la matrice  : ")
        ligne=int(input())
        col = int(input())
        while ligne<=0 or col<=0:
            print(" La ligne ou la colonne invalide: ")
            ligne = int(input())
            col = int(input())

        assert ligne > 0 and col>0
    except TypeError:
        print("Type de données Invalide !")
    except AssertionError:
        print("La taille doit être strictement positive ")
    else:
        return ligne,col

if __name__ == '__main__':
    matrice1=[]
    liste1=[]
    newlist=list()
    matrice2=[]
    produit=[]
    Message1="Matrice 1"
    message2="Remplissage de la matrice :"
    print(Message1.upper().center(50))
    print(message2.upper().center(50))
    ligne1,col1=saisi_taille()

    for i in range(ligne1):
        for j in range(col1):
            element1=int(input(f"Element d'indice [{i+1},{j+1}]: "))
            liste1.append(element1)
            if j==col1-1:
               newlist=liste1.copy()
               matrice1.append(newlist)
               liste1.clear()

    print(matrice1)
    Message1 = "Matrice 2"
    print(Message1.upper().center(50))
    print(message2.upper().center(50))
    ligne2, col2 = saisi_taille()

    for i in range(ligne2):
        for j in range(col2):
            element2=int(input(f"Element d'indice [{i+1},{j+1}]: "))
            liste1.append(element2)
            if j==col2-1:
               newlist=liste1.copy()
               matrice2.append(newlist)
               liste1.clear()
    print(matrice2)


    print("PRODUIT DES MATRICES ")
    for i in range(ligne1):
        for j in range(col2):
            calcul = 0
            for t in range(ligne2):
                calcul+=matrice1[i][t]*matrice2[t][j]

            liste1.append(calcul)
            newlist=liste1.copy()

        produit.append(newlist)
        liste1.clear()

    for i in range(ligne1):
        print(*produit[i])
