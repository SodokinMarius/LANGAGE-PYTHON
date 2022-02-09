#coding ut-8
from Test_Package.Anne_Bixextile import Annee_Bixextille
from Test_Package.Test_Package import table
import Test_Package.Anne_Bixextile
import math
if __name__ == '__main__':

    nbr=int(input("Entrez un nombre : "))
table(nbr)
print(f"La factirielle de {nbr} est {round((math.factorial(nbr)),2)}")

try:
     annee=int(input("Veuillez saisir l'année : "))

     assert annee > 0
except ValueError:
    print("La valeure entrée ne correspond pas !")

except NameError:
    print("Cette Variable n'existe pas encore ")
except TypeError:
    print("Le type de variable est incorrect")
except AssertionError:
    print("L'annee doit être strictement positive :")


else :
 Annee_Bixextille(annee)

