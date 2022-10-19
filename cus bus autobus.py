#vlozenie modulov
import tkinter 
from tkinter import Tk
root=Tk()

#nastavenie platna a jeho rezmerov
canvas = tkinter.Canvas(width=500, height=300) 
canvas.pack() 

#premenne
x = 50
x1 = 40
nieco = 0
i = 0

#otvorenie suboru na zistenie kapacity
subor = open('vytazenost_autobusovej_linky.txt', 'r', encoding='utf-8')
kapacita = int(subor.readlines()[0])
subor.close()

def zastavky(): #funkcia na vypisanie zastavok
    #globalne premenne
    global x
    global lajny
    lajny = 0

    #otvorenie suboru a preskocenie prveho riadku
    subor = open('vytazenost_autobusovej_linky.txt', 'r', encoding='utf-8')
    next(subor)
    riadky = subor.readlines()
    
    #zistenie poctu slov v riadku a nasledne podla toho vypisanie nazvov zastavok
    for index, pocet in enumerate(riadky): 
            lajny += 1
            slova = len(pocet.split())
            riadocek = pocet.split()
            if slova == 3:
                canvas.create_text(50,x,font='Arial 20',anchor='w',text=riadocek[2])
            if slova == 4:
                canvas.create_text(50,x,font='Arial 20',anchor='w',text=riadocek[2]+' '+riadocek[3])     
            x += 30
    
    #zatvorenie suboru
    subor.close()

def data(event): #funkcia na vykreslenie dat z textu
    #globalne premenne
    global x1
    global nieco
    global nastupujuci, vystupujuci, obsadenost
    global i
    global lajny, kapacita
    y = 150/kapacita

    #otvorenie suboru a preskocenie prveho riadku
    subor = open('vytazenost_autobusovej_linky.txt', 'r', encoding='utf-8')
    next(subor)
    riadok = subor.readlines()[i]
    
    #vypocet na zistenie obsadenosti
    riadocek = riadok.split()
    nastupujuci = int(riadocek[0])
    vystupujuci = int(riadocek[1])
    nieco += nastupujuci
    obsadenost = nieco - vystupujuci
    nieco = obsadenost

    #podmienky vykreslenia
    if obsadenost <= kapacita and obsadenost != 0:
        canvas.create_rectangle(250,x1,400,x1+20)
        canvas.create_rectangle(251,x1+1,251+(obsadenost*y),x1+20,fill='green',outline='')
    if obsadenost >= kapacita:
        canvas.create_rectangle(250,x1,400+(obsadenost*y-149),x1+20)
        canvas.create_rectangle(251,x1+1,251+(obsadenost*y),x1+20,fill='red',outline='')
    x1 += 30
    i += 1

    #podmienka kedy skoncit program
    if i == lajny:
        quit()
             
#privolanie funkcii
zastavky()
root.bind("<Key>",data)

#aby fungovalo postupne zobrazovanie
root.mainloop()
