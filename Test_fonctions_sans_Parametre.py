#coding: utf-8
def PlusieursParametre(*param,sep=' ',fin='\n'):

    #Convertion du parametre en liste
    param=list(param)
    print(param)
    '''Convertion du contenu de la liste en chaines : Afin
        de pouvoir faire la jointure'''
    for i,parametre in enumerate(param):
        param[i]=str(parametre)

        #Faisons la jointure
    chaine=sep.join(param)
    print(chaine)
    print("Merci à vous")

    # Ajoutons le parametre de fin
    chaine+=fin
    print(chaine,end='')
    print(param)


if __name__ == '__main__':
    PlusieursParametre("Marius", "Yao","SODOKIN",25,104,7890)

   #Transformation d'une liste en paramètre de fonctions
    maliste=["SODOKIN","Yao","Marius",20,30,450]
    print(*maliste)

