import os
import tkinter as tk

from main import Avtobus
def get_Pas():
    global i, k
    value = str(pas.get())
    Avtobus.list_passjir.append(value)

    lbl1 = tk.Label(win, text=Avtobus.list_passjir[i])
    lbl1.grid(row=k, column=3)
    print(Avtobus.list_passjir)
    k = k+1
    i = i + 1
def get_All():
    famvod = str(famila.get())
    kolvod = int(kol.get())
    plus = str(piz.get())
    v1 = int(sp.get())
    v2 = int(mk.get())
    v3 = int(ms.get())
    v4 = 3
    v5 = int(sm.get())
    v6 = int(s.get())
    v = int(vibros.get())
    c = int(zaxod.get())
    Avtobus71 = Avtobus(v1, v2, v3, v4, v5, v6, v, c)
    Avtobus71.posadka()
    Avtobus71.zadan_famil(kolvod, plus, famvod)
    lbl3 = tk.Label(win, text=Avtobus71.posadka())
    lbl3.grid(row=6, column=0)
    lbl2 = tk.Label(win, text=Avtobus.list_passjir)
    lbl2.grid(row=5, column=0)
k = 3
i = 0

win = tk.Tk()
win.config()
win.geometry("1000x500")
win.resizable(False, False)


btk1 = tk.Button(win, text="Доб.фамилию", command=get_Pas)
btk1.grid(row=0, column=6)
btk2 = tk.Button(win, text="Ввод", command=get_All)
btk2.grid(row=0, column=7)
sp = tk.Entry(win, )    #скорость
mk = tk.Entry(win, )    #максимальноме кол-во пассажиров
ms = tk.Entry(win, )    #макс. скорость
pas = tk.Entry(win, )   #список имен пассажиров
sm = tk.Entry(win, )    #наличие свободных мест
s = tk.Entry(win, )     #кол-во мест в автобусе
vibros = tk.Entry(win, )
zaxod = tk.Entry(win, )
vibros.grid(row=3, column=0)
zaxod.grid(row=3, column=1)

famila = tk.Entry(win, )
kol = tk.Entry(win, )
famila.grid(row=4, column=0)
kol.grid(row=4, column=1)
piz = tk.Entry(win,)
piz.grid(row=4, column=2)
sp.grid(row=0, column=0)
spl = tk.Label(win, text="Скорость").grid(row=1, column=0)
mk.grid(row=0, column=1)
mkl = tk.Label(win, text="макс.колво пас").grid(row=1, column=1)
ms.grid(row=0, column=2)
msl = tk.Label(win, text="макс.скорсть").grid(row=1, column=2)
pas.grid(row=0, column=3)
pasl = tk.Label(win, text="список имен").grid(row=1, column=3)
sm.grid(row=0, column=4)
sml = tk.Label(win, text="наличие свободных мест").grid(row=1, column=4)
s.grid(row=0, column=5)
sl = tk.Label(win, text="кол-во мест").grid(row=1, column=5)



win.mainloop()




