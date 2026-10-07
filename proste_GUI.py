import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Przelicznik kulinarny")


goraLabel = tk.Label(text="Przelicznik tłuszczu")

###RAMKA MASLO -> olej

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
maslo_jaka_jednostka.set("gramy")
maslojednostkiCombobox = ttk.Combobox(ramkaMasloOlej,
                                      width=10,
                                      values=["gramy", "mililitry",],
                                      state="readonly",
                                      textvariable= maslo_jaka_jednostka)


# maslojednostkiCombobox.set("gramy")

przejsciowyLabel1 = tk.Label(ramkaMasloOlej,
                             text="----->",
                             width=10)



##### Olej 
olejLabel = tk.Label(ramkaMasloOlej,
                     text="Olej:",
                     width=10
                     #   anchor="e")
                     )

#zmienna wyniowa

olej_wynik = tk.StringVar()

olejileEntry = tk.Entry(ramkaMasloOlej, width=10, background="lightblue",textvariable=olej_wynik)

olejjednostkiCombobox = ttk.Combobox(ramkaMasloOlej,
                                     width=10,
                                     values=["mililitry",
                                             ],
                                     state="readonly")

olejjednostkiCombobox.set("mililitry")


## przeliczenia

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



#####################uruchamianie po kazdym przeliczeniu #####

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
ramkaMasloOlej.pack(padx=(0, 25), pady=(10, 30))

root.mainloop()