
from cgitb import text
from multiprocessing.sharedctypes import Value

from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox, Treeview
from turtle import update
from setuptools import Command
from tkcalendar import *


class Employe():
    count = 0
    objLista = []
    agLista = []

    def __init__(self, dateNaissance, estCommercial, nom, salaire, sexe, situationFamiliale):
        Employe.count += 1
        Employe.objLista.append(self)
        # Employe.agLista.append(f'{Employe.count}')
        self.dateNaissance = dateNaissance
        self.estCommercial = estCommercial
        self.nom = nom
        self.salaire = salaire
        self.sexe = sexe
        self.situationFamiliale = situationFamiliale
        self.salaireNet()

    def salaireNet(self):
        if self.salaire <= 2500 and self.estCommercial == 'oui':
            self.salairnet = self.salaire+500
        elif self.salaire <= 2500 and self.estCommercial == 'no':
            self.salairnet = self.salaire+1000

        elif self.salaire > 2501 and self.salaire < 4166 and self.estCommercial == 'oui':
            self.salairnet = self.salaire+500+(((self.salaire/100)*10)-250)
        elif self.salaire > 2501 and self.salaire < 4166 and self.estCommercial == 'no':
            self.salairnet = self.salaire+1000+(((self.salaire/100)*10)-250)

        elif self.salaire > 4167 and self.salaire < 5000 and self.estCommercial == 'oui':
            self.salairnet = self.salaire+500+(((self.salaire/100)*20)-666)
        elif self.salaire > 4167 and self.salaire < 5000 and self.estCommercial == 'no':
            self.salairnet = self.salaire+1000+(((self.salaire/100)*20)-666)

        elif self.salaire > 5001 and self.salaire < 6666 and self.estCommercial == 'oui':
            self.salairnet = self.salaire+500+(((self.salaire/100)*30)-1166)
        elif self.salaire > 5001 and self.salaire < 6666 and self.estCommercial == 'no':
            self.salairnet = self.salaire+1000+(((self.salaire/100)*30)-1166)

        elif self.salaire > 6667 and self.salaire < 15000 and self.estCommercial == 'oui':
            self.salairnet = self.salaire+500+(((self.salaire/100)*30)-1433)
        elif self.salaire > 6667 and self.salaire < 15000 and self.estCommercial == 'no':
            self.salairnet = self.salaire+1000+(((self.salaire/100)*30)-1433)

        elif self.salaire > 1500 and self.estCommercial == 'oui':
            self.salairnet = self.salaire+500+(((self.salaire/100)*30)-2033)
        elif self.salaire > 1500 and self.estCommercial == 'no':
            self.salairnet = self.salaire+1000+(((self.salaire/100)*30)-2033)
        else:
            self.salairnet = 0000
        s = self.salairnet
        return s


# *----------algunos objetos---------------
d = Employe('$$(O_0)$$', 'no', 'Doha', 10001, 'Femme', 'Celibataire')
mm = Employe('3/18/22', 'oui', 'Ali', 6500, 'Homme', 'Celibataire')
h = Employe('3/18/22', 'oui', 'HAssAN', 10000, 'Homme', 'Celibataire')


def butAjoutt():

    if selection.get() != '' and nomEntry.get() != '' and cal.get() != '' and EntrySalaire.get() != '' and (varsexe.get() == 'Homme' or varsexe.get() == 'Femme'):
        objjj = Employe(cal.get(), varcomer.get(), nomEntry.get(), float(
            EntrySalaire.get()), varsexe.get(), selection.get())
        fnet.delete(0, END)
        fnet.insert(0, (f'{objjj.salairnet} DH'))


def Rechercher():
    winlist = Tk()
    winlist.title('Recherche')

    #!-----------------------treeview----------------------------------------------
    tableau = Treeview(winlist)
    tableau['column'] = ('nom', 'dateNaissance', 'estCommercial',
                         'salaire', 'salairenet', 'sexe', 'situationFamiliale')
    tableau.column('#0', width=20)
    tableau.column('nom', width=150, anchor='center')
    tableau.column('dateNaissance', width=120, anchor='center')
    tableau.column('estCommercial', width=110, anchor='center')
    tableau.column('salaire', width=150, anchor='center')
    tableau.column('salairenet', width=160, anchor='center')
    tableau.column('sexe', width=120, anchor='center')
    tableau.column('situationFamiliale', width=120, anchor='center')
    tableau.heading('#0', text='', anchor='center')
    tableau.heading('nom', text='Nom', anchor='center')
    tableau.heading('dateNaissance', text='Date Naissance', anchor='center')
    tableau.heading('estCommercial', text='Commercial', anchor='center')
    tableau.heading('salaire', text='Salaire', anchor='center')
    tableau.heading('salairenet', text='Salaire(NET)', anchor='center')
    tableau.heading('sexe', text='sexe', anchor='center')
    tableau.heading('situationFamiliale',
                    text='Situation Familiale', anchor='center')

    tableau.pack(padx=10, pady=10)
    # hlistLabel=Label(winlist,text="--{nom}--{dateNaissance}--{estCommercial}--{salaire}DH--{salairenet}DH--{sexe}--{situationFamiliale}--")
    # hlistLabel.pack()
    cn = 0
    for lmt in Employe.objLista:

        if nomEntry.get() == lmt.nom:
            cn += 1   #?count
            # listLabel=Label(winlist,text=f"--{lmt.nom}--{lmt.dateNaissance}--{lmt.estCommercial}--{lmt.salaire}DH--{lmt.salairnet}DH--{lmt.sexe}--{lmt.situationFamiliale}--")
            # listLabel.pack()
            s = str(lmt.salaire)+" DH"
            sn = str(lmt.salairnet)+' DH'
            tableau.insert(parent="", index='end', iid=cn, text="", values=(
                lmt.nom, lmt.dateNaissance, lmt.estCommercial, s, sn, lmt.sexe, lmt.situationFamiliale))


def liste():
    winlist = Tk()
    winlist.title('Liste')
    tableau = Treeview(winlist)
    tableau['column'] = ('nom', 'dateNaissance', 'estCommercial',
                         'salaire', 'salairenet', 'sexe', 'situationFamiliale')
    tableau.column('#0', width=20)
    tableau.column('nom', width=150, anchor='center')
    tableau.column('dateNaissance', width=120, anchor='center')
    tableau.column('estCommercial', width=110, anchor='center')
    tableau.column('salaire', width=150, anchor='center')
    tableau.column('salairenet', width=160, anchor='center')
    tableau.column('sexe', width=120, anchor='center')
    tableau.column('situationFamiliale', width=120, anchor='center')
    tableau.heading('#0', text='', anchor='center')
    tableau.heading('nom', text='Nom', anchor='center')
    tableau.heading('dateNaissance', text='Date Naissance', anchor='center')
    tableau.heading('estCommercial', text='Commercial', anchor='center')
    tableau.heading('salaire', text='Salaire', anchor='center')
    tableau.heading('salairenet', text='Salaire(NET)', anchor='center')
    tableau.heading('sexe', text='sexe', anchor='center')
    tableau.heading('situationFamiliale',
                    text='Situation Familiale', anchor='center')

    tableau.pack(padx=10, pady=10)
    # hlistLabel=Label(winlist,text="--{nom}--{dateNaissance}--{estCommercial}--{salaire}DH--{salairenet}DH--{sexe}--{situationFamiliale}--")
    # hlistLabel.pack()
    cn = 0
    for lmt in Employe.objLista:
        cn += 1
        s = str(lmt.salaire)+" DH"
        sn = str(lmt.salairnet)+' DH'

        tableau.insert(parent="", index='end', iid=f'{cn}', text="", values=(
            lmt.nom, lmt.dateNaissance, lmt.estCommercial, s, sn, lmt.sexe, lmt.situationFamiliale))

        # winlist.pack()
        # listLabel=Label(winlist,text=f"--{lmt.nom}--{lmt.dateNaissance}--{lmt.estCommercial}--{lmt.salaire}DH--{lmt.salairnet}DH--{lmt.sexe}--{lmt.situationFamiliale}--")
        # listLabel.pack()
# ---------------------------------------------------------------------------------------------------------------


win = Tk()
win.geometry("600x300")
win.title("Employe")
# frames 4 inputs-------------------------------------------------------------------
inputs = LabelFrame(win, padx=8, pady=8)
inputs.grid(row=0, column=0)

# ----------------------------------------------------------------------------------
nom = Label(inputs, text="Nom   ", pady=5).grid(row=0, column=0, sticky=W)
nomEntry = Entry(inputs, width=25)
nomEntry.grid(row=0, column=1, sticky=W)
salario = Label(inputs, text="salaire", pady=5).grid(row=3, column=0, sticky=W)
EntrySalaire = Entry(inputs, width=25)
EntrySalaire.grid(row=3, column=1, sticky=W)
# calender
dateN = Label(inputs, text="Date de naissance",
              pady=5).grid(row=1, column=0, sticky=W)
cal = DateEntry(inputs, width=20, background="#8f8c8c",
                foreground="white", bd=2)
cal.grid(row=1, column=1, sticky=W)
# !select----------------------------------------------------------------------------
SituationFamiliale = Label(inputs, text="Situation Familiale", pady=5).grid(
    row=4, column=0, sticky=W)
elijedos = ['Celibataire', 'Marrie']
# option0=StringVar(inputs)
# option0.set(elijedos[0])
selection = ttk.Combobox(inputs, values=elijedos)
selection.grid(row=4, column=1, sticky=W)
selection.current(0)
selection.bind("<<ComboboxSelected>>")
# selection['values']=('Celibataire','Marrie')
# update(elijedos)
# ?fram------------------------------------------radio----------------------------------------------
varsexe = StringVar()
sexe = LabelFrame(win, text="sexe", bd=1, padx=100, pady=1)
sexe.grid(row=1, column=0, padx=10, pady=1)
# algo=Label(sexe,text="Sexe").grid()
sexe1 = Radiobutton(sexe, text='Homme', variable=varsexe, value='Homme')
sexe1.grid(pady=5)
sexe1.select()
sexe2 = Radiobutton(sexe, text='Femme', variable=varsexe, value='Femme')
sexe2.grid(pady=5)
sexe2.deselect()

# checkbutton-------------------------------------------------------------------------------
varcomer = StringVar()
comer = Checkbutton(win, text="Commercial",
                    variable=varcomer, onvalue='oui', offvalue='no')
comer.grid(row=2, column=0)
comer.deselect()

# la ultima frame
finalfream = LabelFrame(win).grid()
fnettext = Label(finalfream, text='Salaire net    ').grid(
    row=10, column=0, sticky=E)
fnet = Entry(finalfream, width=25)
fnet.grid(row=10, column=1)
# frame buttones-------------------------------------------------------------------------------------
butframe = LabelFrame(win, bd=0)
butframe.grid(row=0, column=1, columnspan=1, rowspan=2, sticky=SE)
butAjou = Button(butframe, text='Ajouter', padx=50, pady=8, command=butAjoutt)
butAjou.grid(row=0, column=2, padx=10, pady=15, sticky=NE)
butRech = Button(butframe, text='Rechercher', padx=40, pady=8, command=Rechercher).grid(
    row=1, column=2, padx=10, pady=15, sticky=NE)
butList = Button(butframe, text='Liste', padx=58, pady=8, command=liste)
butList.grid(row=2, column=2, padx=10, pady=15, sticky=NE, rowspan=1)
#!=-------=
#region
win.mainloop()
print(Employe.objLista[0].nom)
# print(objjj.salairenet)
# endregion
#!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%1%%%
# ?[Toplevel widget Label widget Button widgetCanvas widget Checkbutton widget Entry widgetFrame widget LabelFrame widget Listbox widgetMenu widget Menubutton widget Message widgetOptionMenu widget PanedWindow widget Radiobutton widgetScale widget Scrollbar widget Spinbox widgetText widget Bitmap Class widget Image Class widget]
#!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
