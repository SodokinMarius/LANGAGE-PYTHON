#coding: utf-8
from tkinter.messagebox import *
import tkinter

if __name__ == '__main__':

    from tkinter import *
    def affiche():
        print("WELCOME")
        print(Value.get())
        print(bt1.get())
        print(bt2.get())
        print(bt3.get())
        print(bout1.get())
        print(bout2.get())
        print(liste)
        print(callback())

    root=tkinter.Tk()
    root.title("MON PREMIER INTERFACE TKINTER")
    root["bg"] = "pink"
    # Canevas
    cnv = Canvas(root, width=500, height=400)
    cnv.pack()
    #label
    text=tkinter.Label(cnv,text="WELCOME TO MY FIRST APPLICATION",width=40,height=5,bg="ivory")
   #Affichons le texte cree
    text.pack(padx=20,pady=20)


    root.resizable(False,False)#Blocage des diemnsions
#Creation d'un bouton
    bouton=tkinter.Button(cnv,text="QUITER",command=affiche)
    bouton.pack(side="bottom")
    cnv2 = Canvas(root, width=400, height=400)
    cnv.pack()
    #creation des input

    Value=tkinter.StringVar() #Un type de variable
    Value.set("Entrer une chaine :")
    entree=Entry(root,textvariable=Value,width=30)
    entree.pack()

    #Les boutons radio
    radio=StringVar()
    bt1=Radiobutton(root,text="oui",variable=radio,value=1)
    bt2 = Radiobutton(root, text="non", variable=radio, value=2)
    bt3 = Radiobutton(root, text="Je ne sais pas", variable=radio, value=3)
    bt1.pack()
    bt2.pack()
    bt3.pack()

    #Cases à cocher
    bout1=Checkbutton(root,text="Nouveau")
    bout2= Checkbutton(root, text="Ancien")
    #radio.pack()
    bout1.pack()
    bout2.pack()
    print(" ")

    #Les listes
    liste=Listbox(root)
    liste.insert(1,"Python")
    liste.insert(2,"JAVA")
    liste.insert(3,"PHP")
    liste.insert(4,"JavaScript")
    liste.insert(5,"C")
    liste.insert(6,"C++")
    liste.insert(7,"HTML")
    liste.insert(8,"CSS")
    liste.pack()


    #Les alertes
    def callback():
        if askyesno("QUITER","Vous êtes sûr de vouloir quitter ?"):
            showwarning("Non","CA NE NOUS CONSERNE PLUS")
        else:
            showinfo("BON","VOUS AVEZ PEUR ?")
            showerror("PHP","Vous êtes fort")
        Button(text="Action",command=callback).pack()




    root.mainloop()

