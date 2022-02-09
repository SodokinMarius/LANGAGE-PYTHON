#coding: utf-8

from Test_Package import  Anne_Bixextile
def salut():
    print("Je vous salut tous , c'est moi Yao Marius SODOKIN")
if __name__ == '__main__':

    echiquier={}
    echiquier[1,'A']="Couleur Blanc"
    echiquier[2, 'A'] = "Couleur Bleue"
    echiquier[3, 'A'] = "Couleur Bleue nuit"
    echiquier[1, 'B'] = "Couleur Rouge"
    echiquier[2, 'B'] = "Couleur rouge sombre"
    echiquier[3, 'B'] = "Couleur Rouge sang"
    echiquier[1, 'C'] = "Couleur vert"
    echiquier[2, 'C'] = "Couleur vert nuit"
    echiquier[3, 'D'] = "Couleur vert claire"

    print("\n",str(echiquier))
    del echiquier[1,'A']

    print("\n",str(echiquier))
    print(echiquier.pop((2,'C')))
    #print(suprimer)
    print("\n", str(echiquier))
    #help(dict)


    #STOCKAGE DICTIONNAIRE DANS DES FONCTIONS
    dictFonction={}
    dictFonction["anne"]=Anne_Bixextile.Annee_Bixextille(2014)
    dictFonction["salut"]=salut

    (dictFonction["salut"]())

    #Parcourrir et afficher le contenu d'un dictionnaire
    print("Les clès du dictionnaire Echiquier :")
    for cle in echiquier.keys():
        print(cle)

#Parcours des valeurs
print("Les valeurs du dictionnaire Echiquier :")
for valeur in echiquier.values():
    print(valeur)

    #L'apperçu complet du dictionnaire
    print("L'apperçu complet du dictionnaire")
    for cle, valeur in echiquier.items():
        print(" {}  ===> {} ".format(cle,valeur) )
