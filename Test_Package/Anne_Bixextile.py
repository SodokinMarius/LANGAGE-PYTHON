 #coding utf-8
def Annee_Bixextille(annee):
      if annee%4==0 and annee%100!=0  or annee%400==0:
          print(f"{annee} est bixesstille")
      else:
          print(f"{annee} est une annee  non bixextille ")

if __name__ == '__main__':

 anne=int(input("Saisir une annee svp : "))
 Annee_Bixextille(anne)