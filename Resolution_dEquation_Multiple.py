#coding : utf-8
def separateur(chaine):
    liste1=list()
    liste1=chaine.split(" ")
    a=float(liste1[0][0])
    sign = liste1[1]
    b=float(liste1[2])
    c=float(liste1[4])
    return a,b,c,sign

def Resolution(chaine):
    a,b,c,sign=separateur(chaine)
    if a==0:
        if((c-b)!=0):
            message="No solution"
        elif (c-b)==0:
            message="More than one solution"
        return message
    else:
        return (c-b)/a


if __name__ == '__main__':
    solution=list()
    ValeurNormale=0

    while(ValeurNormale!=1):
          P=int(input("Enter :"))
          if(P>=1 and P<1000):
              ValeurNormale=1
    tailNormale=0
 #except NameError:
   #  print("Ce nom n'existe pas !")
 #else:
    for i in range(P) :
         # while(tailNormale!=0):
          equation=input()
              #if len(equation)<200:
               #   tailNormale=1
          solut=Resolution(equation)
          solution.append(solut)

    for i in range(P):
        print("Equation :  {}".format(i+1))
        print("x = {} " .format(solution[i]))