import pandas as pd
from tkinter import *
import matplotlib.pyplot as plt

dane=pd.read_excel(r"C:\Users\Asus\Desktop\Studia_Informatyka_i_Ekonometria\Python\pythonProject3\podstawowe_dane_z_badania_aktywnosci_ekonomicznej_ludnosci_wyrownane_sezonowo_mar.xlsx")
stopa_bezrobocia = dane.loc[416:467, ['Rok', 'Kwartał', 'Wartość']]
stopa_bezrobocia_group = stopa_bezrobocia.groupby('Rok').agg(Srednia=('Wartość', lambda x: round(x.mean(), 2)))
stopa_bezrobocia_wykres = stopa_bezrobocia.groupby('Rok').agg(Rok=('Rok', 'max'), Srednia=('Wartość', 'mean'))


st_b = {}

for rok in range(2010, 2023):
    st_b[rok] = dane.loc[4 * (rok - 2010) + 416: 4 * (rok - 2010) + 419, ['Rok', 'Kwartał', 'Wartość']]


root = Tk()
root.title('Bezrobocie')
root.geometry("1200x600")
t1 = Label(root, text='Stopa bezrobocia (w %) w latach 2010-2022:', bg='blue', width=50, height=3)
t1.grid(column=1, row=1)

l1 = Label(root, text=stopa_bezrobocia_group)
l1.grid(column=1, row=2, rowspan=13)


def wykres():
    fig, ax = plt.subplots()
    os_x = stopa_bezrobocia_wykres['Rok']
    os_y = stopa_bezrobocia_wykres['Srednia']
    ax.bar(os_x, os_y)
    ax.set_xlabel('Lata')
    ax.set_ylabel('Stopa bezrobocia (w %)')
    ax.set_title('Stopa bezrobocia (w %) w poszczegolnych latach')
    plt.show()


przycisk = Button(root, text="Pokaż wykres stopy bezrobocia\nw poszczególnych latach", command=wykres)
przycisk.grid(column=1, row=15)

t2 = Label(root, text="Wybierz, co chcesz wyświetlić:", bg='green', width=60, height=3)
t2.grid(column=2, row=1)

v1 = StringVar()


def maximum():
    wynik = str(stopa_bezrobocia.Wartość.max())+"%"
    l2.config(text=wynik)


def minimum():
    wynik = str(stopa_bezrobocia.Wartość.min())+"%"
    l2.config(text=wynik)


def srednia():
    wynik = str(round(stopa_bezrobocia.Wartość.mean(),2))+"%"
    l2.config(text=wynik)


max=Radiobutton(root, text="Maksymalna wartość stopy bezrobocia w latach 2010-2022", variable=v1, value=1, command=maximum)
max.grid(column=2, row=2, rowspan=4)
min=Radiobutton(root, text="Minimalna wartość stopy bezrobocia w latach 2010-2022", variable=v1, value=2, command=minimum)
min.grid(column=2, row=6, rowspan=4)
sr=Radiobutton(root, text="Średnia wartość stopy bezrobocia w latach 2010-2022", variable=v1, value=3, command=srednia)
sr.grid(column=2, row=10, rowspan=4)

v1.set(-1)

l2 = Label(root, bg='green', width=30, height=3)
l2.grid(column=2, row=15)

t3 = Label(root, text="Wybierz rok, z którego chcesz wyświetlić dane: ", bg='yellow', width=60, height=3)
t3.grid(column=3, row=1)

v2 = StringVar()


def analiza_roku(rok):
    dane_roku = st_b.get(rok)
    a = "Średnia wartość stopy bezrobocia wynosi:\n" + str(round(dane_roku['Wartość'].mean(), 2)) + "%" + \
        "\nNajwyższa kwartalna wartość stopy bezrobocia wynosi:\n" + str(dane_roku['Wartość'].max()) + "%" + \
        "\nNajniższa kwartalna wartość stopy bezrobocia wynosi:\n" + str(dane_roku['Wartość'].min()) + "%"
    l3.config(text=a)


_2010=Radiobutton(root, text="2010", variable=v2, value=1, command=lambda: analiza_roku(2010))
_2010.grid(column=3, row=2)
_2011=Radiobutton(root, text="2011", variable=v2, value=2, command=lambda: analiza_roku(2011))
_2011.grid(column=3, row=3)
_2012=Radiobutton(root, text="2012", variable=v2, value=3, command=lambda: analiza_roku(2012))
_2012.grid(column=3, row=4)
_2013=Radiobutton(root, text="2013", variable=v2, value=4, command=lambda: analiza_roku(2013))
_2013.grid(column=3, row=5)
_2014=Radiobutton(root, text="2014", variable=v2, value=5, command=lambda: analiza_roku(2014))
_2014.grid(column=3, row=6)
_2015=Radiobutton(root, text="2015", variable=v2, value=6, command=lambda: analiza_roku(2015))
_2015.grid(column=3, row=7)
_2016=Radiobutton(root, text="2016", variable=v2, value=7, command=lambda: analiza_roku(2016))
_2016.grid(column=3, row=8)
_2017=Radiobutton(root, text="2017", variable=v2, value=8, command=lambda: analiza_roku(2017))
_2017.grid(column=3, row=9)
_2018=Radiobutton(root, text="2018", variable=v2, value=9, command=lambda: analiza_roku(2018))
_2018.grid(column=3, row=10)
_2019=Radiobutton(root, text="2019", variable=v2, value=10, command=lambda: analiza_roku(2019))
_2019.grid(column=3, row=11)
_2020=Radiobutton(root, text="2020", variable=v2, value=11, command=lambda: analiza_roku(2020))
_2020.grid(column=3, row=12)
_2021=Radiobutton(root, text="2021", variable=v2, value=12, command=lambda: analiza_roku(2021))
_2021.grid(column=3, row=13)
_2022=Radiobutton(root, text="2022", variable=v2, value=13, command=lambda: analiza_roku(2022))
_2022.grid(column=3, row=14)

v2.set(-1)

l3 = Label(root, bg='yellow', width=50, height=10)
l3.grid(column=3, row=15)

root.mainloop()