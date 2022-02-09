import random
import math
#coding utf-8

if __name__ == '__main__':
 continuer=1

 decision='n'

 argent = float(input("Entrez le montant que vous posedez : "))
 while(argent<=0):
        argent=float(input("Montant Invalide ! Saisir une valeure strictement positive : "))

 while(continuer==1):

    try:
             numero_mise=int(input("Entrez le numero sur lequel vous miser : "))

             somme_mise=float(input(("Entrer la somme de votre mise : ")))
             assert  numero_mise>0 and numero_mise<50 and somme_mise>0 and argent>=somme_mise
    except TypeError :
            print("Le type n'est pas valide !")
    except ValueError:
            print("La valeur entrée n'est pas conforme !")
    except AssertionError:
            print("Le numero doit être compris entre 0 et 50  ou la somme doite être strictement pospitive")
    else :

                numero_roulette=random.randrange(50)
                print(f"Roulette: {numero_roulette} et Numero mise :{numero_mise}")
                if(numero_mise==numero_roulette):
                    gain=3*somme_mise
                    argent+=gain
                    print(f"Bravo ! Vous avez gagné ! et votre gain est de {gain} $")
                elif (numero_mise%2==0 and numero_roulette%2==0) or (numero_mise%2==1 and numero_roulette%2==1):
                    gain=math.ceil(somme_mise/2)
                    argent+=gain
                    print(f"Vous avez gragné à moitié ! et Votre gain est {gain} $")
                else:
                    argent-=somme_mise
                    print("Désolé ! Vous êtes en perte")
                    if argent<=0:
                        print("Votre  argent est epuisé ! Vous avez donc perdu ! ")
                        continuer=0
                        break

                print(f"Il vous reste {argent} $")
                decision = input("Voulez vous  continuer ? (O/N)")
                if(decision=='N' or decision=='n'):
                    continuer=0


