import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Przelicznik kulinarny")

ramkaMasloOlej = tk.Frame(root)

goraLabel = tk.Label(text="Przelicznik tłuszczu")

masloLabel = tk.Label(ramkaMasloOlej,
                      text="Masło:",
                      width=10
                      #   anchor="e")
                      )

masloileEntry = tk.Entry(ramkaMasloOlej, width=10, background="lightblue")
maslojednostkiCombobox = ttk.Combobox(ramkaMasloOlej,
                                      width=10,
                                      values=["gramy", "mililitry",
                                              "łyżki", "łyżeczki"],
                                      state="readonly")

przejsciowyLabel1 = tk.Label(ramkaMasloOlej,
                             text="----->",
                             width=10)


olejLabel = tk.Label(ramkaMasloOlej,
                     text="Olej:",
                     width=10
                     #   anchor="e")
                     )
olejileEntry = tk.Entry(ramkaMasloOlej, width=10, background="lightblue")

olejjednostkiCombobox = ttk.Combobox(ramkaMasloOlej,
                                     width=10,
                                     values=["gramy", "mililitry",
                                             "łyżki", "łyżeczki"],
                                     state="readonly")

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

oddzielnik = tk.Label(text="Przelicznik miar",
                      padx=10, pady=10)

oddzielnik.pack(expand=True,
                padx=(20, 20), pady=10)

ramka2 = tk.Frame(root)

#############  CUKIER  ##########
cukierLabel = tk.Label(ramka2,
                       text="Cukier",
                       width=10)

cukierEntry = tk.Entry(ramka2, width=10, bg="pink")
cukierComBox = ttk.Combobox(ramka2,
                            width=10,
                            values=["gram", "kilogram", "mililitr", "litr", ],
                            state="readonly")

przerywnikCukier = tk.Label(ramka2, text="-->", width=10)

cukierKubkiEntry = tk.Entry(ramka2, width=10, bg="MediumPurple1")
cukierKubkiComBox = ttk.Combobox(ramka2,
                                 width=10,
                                 values=["łyżeczka", "łyżka", "szklanka", ],
                                 state="readonly")


cukierLabel.grid(row=0, column=0)
cukierEntry.grid(row=0, column=1)
cukierComBox.grid(row=0, column=2)
przerywnikCukier.grid(row=0, column=3)
cukierKubkiEntry.grid(row=0, column=4)
cukierKubkiComBox.grid(row=0, column=5)

#############  /CUKIER  ##########
#### mąka#######

makaLabel = tk.Label(ramka2,
                     text="Mąka",
                     width=10)

makaEntry = tk.Entry(ramka2, width=10, bg="pink")
makaComBox = ttk.Combobox(ramka2,
                          width=10,
                          values=["gram", "kilogram", "mililitr", "litr", ],
                          state="readonly")

przerywnikmaka = tk.Label(ramka2, text="-->", width=10)

makaKubkiEntry = tk.Entry(ramka2, width=10, bg="MediumPurple1")
makaKubkiComBox = ttk.Combobox(ramka2,
                               width=10,
                               values=["łyżeczka", "łyżka", "szklanka", ],
                               state="readonly")


makaLabel.grid(row=1, column=0)
makaEntry.grid(row=1, column=1)
makaComBox.grid(row=1, column=2)
przerywnikmaka.grid(row=1, column=3)
makaKubkiEntry.grid(row=1, column=4)
makaKubkiComBox.grid(row=1, column=5)
### /Mąka###


########### Masło #########
masloLabel = tk.Label(ramka2,
                      text="Masło",
                      width=10)

masloEntry = tk.Entry(ramka2, width=10, bg="pink")
masloComBox = ttk.Combobox(ramka2,
                           width=10,
                           values=["gram", "kilogram", "mililitr", "litr", ],
                           state="readonly")

przerywnikmaslo = tk.Label(ramka2, text="-->", width=10)

masloKubkiEntry = tk.Entry(ramka2, width=10, bg="MediumPurple1")
masloKubkiComBox = ttk.Combobox(ramka2,
                                width=10,
                                values=["łyżeczka", "łyżka", "szklanka", ],
                                state="readonly")


masloLabel.grid(row=2, column=0, pady=(0, 20))
masloEntry.grid(row=2, column=1, pady=(0, 20))
masloComBox.grid(row=2, column=2, pady=(0, 20))
przerywnikmaslo.grid(row=2, column=3, pady=(0, 20))
masloKubkiEntry.grid(row=2, column=4, pady=(0, 20))
masloKubkiComBox.grid(row=2, column=5, pady=(0, 20))

############# /MASŁO   #########

ramka2.pack()

root.mainloop()
