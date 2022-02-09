def table(nbr, max=10) -> object:
    i = 0
    print(" Le table de multiplication  : ")
    while i < max:

            print(f"{i+1} x {nbr} = {(i+1)* nbr}")
            i+=1


#coding utf-8
if __name__ == '__main__':
    nbr=int(input("Veuillez entrer un nombre : "))
    table(nbr)

