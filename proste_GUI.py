import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Przelicznik kulinarny")


goraLabel = tk.Label(text="Przelicznik tłuszczu")

##### RAMKA MASLO -> OLEJ

ramkaMasloOlej = tk.Frame(root)

masloLabel = tk.Label(ramkaMasloOlej,
                      text="Masło:",
                      width=10
                      #   anchor="e")
                      )

####ta jednostka przechowuje wartosc masla, najpierw wywolana przez StringVar, a potem pojawia sie jako argument textvariable w widgecie Entry masloileEntry
maslo_ile_wartosc = tk.StringVar()

masloileEntry = tk.Entry(ramkaMasloOlej, width=10, background="pink", textvariable=maslo_ile_wartosc)

maslo_jaka_jednostka = tk.StringVar()
maslojednostkiCombobox = ttk.Combobox(ramkaMasloOlej,
                                      width=10,
                                      values=["gramy", "mililitry",],
                                      state="readonly",
                                      textvariable=maslo_jaka_jednostka)
maslo_jaka_jednostka.set("gramy")

# maslojednostkiCombobox.set("gramy")

przejsciowyLabel1 = tk.Label(ramkaMasloOlej,
                             text="----->",
                             width=10)


### Olej ###
olejLabel = tk.Label(ramkaMasloOlej,
                     text="Olej:",
                     width=10
                     #   anchor="e")
                     )
olej_wynik = tk.StringVar()
olejileEntry = tk.Entry(ramkaMasloOlej, width=10, background="lightblue", textvariable=olej_wynik)

olejjednostkiCombobox = ttk.Combobox(ramkaMasloOlej,
                                     width=10,
                                     values=["mililitry",
                                             ],
                                     state="readonly")

olejjednostkiCombobox.set("mililitry")


######przeliczenia ####
def przelicz_maslo_na_olej(*args):
    try:
        #pobieram co wpisano do Entry maslo
        maslo = float(maslo_ile_wartosc.get().replace(",","."))

        #pobieram jaka jednostke wybrano
        jednosta = maslo_jaka_jednostka.get()

        if jednosta == "gramy":
            olej = maslo * 0.8

        elif jednosta == "mililitry":
            olej = maslo * 0.75

        olej_wynik.set(round(olej,2))

    except ValueError:
        olej_wynik.set(maslo_ile_wartosc.get())

maslo_ile_wartosc.trace_add("write",przelicz_maslo_na_olej) #ponownie policzy przy zmianie w polu Entry maslo
maslo_jaka_jednostka.trace_add("write",przelicz_maslo_na_olej) #ponownie przeliczy przy zmianie jednostki


masloLabel.pack(side=tk.LEFT)
masloileEntry.pack(side=tk.LEFT)
maslojednostkiCombobox.pack(side=tk.LEFT)
przejsciowyLabel1.pack(side=tk.LEFT)
olejLabel.pack(side=tk.LEFT)
olejileEntry.pack(side=tk.LEFT)
# olejjednostkiCombobox.pack(side=tk.LEFT, padx=(0, 10), pady=(10, 10))
olejjednostkiCombobox.pack(side=tk.LEFT)

goraLabel.pack(expand=True, padx=10, pady=10)
ramkaMasloOlej.pack(padx=(0, 25), pady=(10, 10))




######################## Ramka Olej -> Maslo
ramkaOlejMaslo = tk.Frame(root)

olej_Label = tk.Label(ramkaOlejMaslo,
                      text="Olej:",
                      width=10
                      #   anchor="e")
                      )

ile_oleju = tk.StringVar()

olej_ile_Entry = tk.Entry(ramkaOlejMaslo, width=10, background="lightblue",textvariable=ile_oleju)
Olej_ile_Combobox = ttk.Combobox(ramkaOlejMaslo,
                                      width=10,
                                      values=["mililitry",],
                                      state="readonly")

Olej_ile_Combobox.set("mililitry")

przejsciowyLabel1 = tk.Label(ramkaOlejMaslo,
                             text="----->",
                             width=10)


maslo_Label = tk.Label(ramkaOlejMaslo,
                     text="Masło:",
                     width=10
                     #   anchor="e")
                     )
ile_masla = tk.StringVar()

maslo_Entry = tk.Entry(ramkaOlejMaslo, width=10, background="pink",textvariable=ile_masla)

jaka_jednostka_masla = tk.StringVar()

maslo_jednostki_Combobox = ttk.Combobox(ramkaOlejMaslo,
                                     width=10,
                                     values=["gramy","mililitry",
                                             ],
                                     state="readonly",
                                     textvariable=jaka_jednostka_masla)

maslo_jednostki_Combobox.set("gramy")

def przelicz_olej_na_maslo(*args):
    try:
        #pobierz co wpisano w Entry Olej
        olej_olej = float(ile_oleju.get().replace(",","."))

        #pobierz jaka jednostke miary wybrano

        jednostka_miary = jaka_jednostka_masla.get()

        if jednostka_miary == "gramy":
            maslo = olej_olej *1.25

        elif jednostka_miary =="mililitry":
            maslo = olej_olej * 1.33

        ile_masla.set(round(maslo,2))

    except: 
        ile_masla.set("xd")   

##########uruchamianie po kazdym wpisanu #####
ile_oleju.trace_add("write",przelicz_olej_na_maslo)
jaka_jednostka_masla.trace_add("write",przelicz_olej_na_maslo)

            



olej_Label.pack(side=tk.LEFT)
olej_ile_Entry.pack(side=tk.LEFT)
Olej_ile_Combobox.pack(side=tk.LEFT)
przejsciowyLabel1.pack(side=tk.LEFT)
maslo_Label.pack(side=tk.LEFT)
maslo_Entry.pack(side=tk.LEFT)
# maslo_jednostki_Combobox.pack(side=tk.LEFT, padx=(0, 10), pady=(10, 10))
maslo_jednostki_Combobox.pack(side=tk.LEFT)

goraLabel.pack(expand=True, padx=10, pady=10)
ramkaOlejMaslo.pack(padx=(0, 25), pady=(10, 30))









root.mainloop()