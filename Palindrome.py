
if __name__ == '__main__':
    liste1=list()
    liste2=list()

    ann_list1="LISTE 1 : "
    ann_list2="LISTE 2 : "
    tail=int(input("Entrer la taille des listes : "))
    print(ann_list1.center(50))
    for i in range(0,tail):
         element1=input("Enter l' élément {} : ".format(i+1))
         liste1.append(element1)

    print(ann_list2.center(50))
    for i in range(0,tail):
        element2=input("Entrer l  'élément {}".format(i+1))
        liste2.append(element2)


    print(liste1)
    print(liste2)
    liste1.pop()
    liste2.insert(3,"yyffy")
    print(f"liste1 : {liste1} ")
    print(f"liste1 Inverse : {liste1.reverse()} ")
    print(liste2)

print(liste1+liste2)
messagePalindrome="Verification Palindrôme"
print(messagePalindrome.upper().center(50))
if(liste1==(liste1.reverse())):
     print("La liste 1 est palindrôme")
else:
    print("La liste 1 n'est pas palindrome")

liste4=" ".join(liste1)
liste3=messagePalindrome.split(" ")
print(f"liste3 : {liste3}")
print(liste4)