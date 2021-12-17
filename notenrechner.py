from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Bachelor Notenrechner")

root.geometry("800x700")

#Anweisungen

instruction_1 = Label(root, text = "Put ya grades in")
instruction_1.place(x = 300, y = 20)

instruction_2 = Label(root, text = "Wenn Modul oder Note nicht vorhanden, 0 eintragen")
instruction_2.place(x = 250, y = 40)

#Hauptfach

title_1 = Label(root, text = "Hauptfach: ")
title_1.place(x = 50, y = 40)

#Platzhalter + Funktion

placeholdern = "Note"
placeholderects = "ECTS"

class placeholder_entry(ttk.Entry):
    def __init__(self, container, placeholder, *args, **kwargs):
        super().__init__(container, *args, style="Placeholder.TEntry", **kwargs)
        self.placeholder = placeholder
        
        self.insert("0", self.placeholder)
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
        
    def _clear_placeholder(self, e):
        if self["style"] == "Placeholder.TEntry":
            self.delete("0", "end")
            self["style"] = "TEntry"
            
    def _add_placeholder(self, e):
            if not self.get():
                self.insert("0", self.placeholder)
                self["style"] = "Placeholder.TEntry"

style = ttk.Style(root)
style.configure("Placeholder.TEntry", foreground="#585858")

#Modul 1 Berechnung

title_1_1 = Label(root, text = "Modul 1: ")
title_1_1.place(x = 50, y = 75)


hfn_entry_1 = placeholder_entry(root, "Note", width = 15)
hfn_entry_1.place(x = 50, y= 100)

hfects_entry_1 = placeholder_entry(root, "ECTS", width = 15)
hfects_entry_1.place(x = 50, y = 125)

#Modul 2 Berechnung

title_1_2 = Label(root, text = "Modul 2: ")
title_1_2.place(x = 50, y = 150)

hfn_entry_2 = placeholder_entry(root, "Note", width = 15)
hfn_entry_2.place(x = 50, y = 175)

hfects_entry_2 = placeholder_entry(root, "ECTS", width = 15)
hfects_entry_2.place(x = 50, y = 200)

#Modul 3 Berechnung

title_1_3 = Label(root, text = "Modul 3: ")
title_1_3.place(x = 50, y = 225)

hfn_entry_3 = placeholder_entry(root, "Note", width = 15)
hfn_entry_3.place(x = 50, y = 250)

hfects_entry_3 = placeholder_entry(root, "ECTS", width = 15)
hfects_entry_3.place(x = 50, y = 275)

#Modul 4 Berechnung

title_1_4 = Label(root, text = "Modul 4: ")
title_1_4.place(x = 150, y = 75)

hfn_entry_4 = placeholder_entry(root, "Note", width = 15)
hfn_entry_4.place(x = 150, y = 100)

hfects_entry_4 = placeholder_entry(root, "ECTS", width = 15)
hfects_entry_4.place(x = 150, y = 125)

#Berechnung Modul 5

title_1_5 = Label(root, text = "Modul 5: ")
title_1_5.place(x = 150, y = 150)

hfn_entry_5 = placeholder_entry(root, "Note", width = 15)
hfn_entry_5.place(x = 150, y = 175)

hfects_entry_5 = placeholder_entry(root, "ECTS", width = 15)
hfects_entry_5.place(x = 150, y = 200)

#Berechnung Modul 6

title_1_6 = Label(root, text = "Modul 6: ")
title_1_6.place(x = 150, y = 225)

hfn_entry_6 = placeholder_entry(root, "Note", width = 15)
hfn_entry_6.place(x = 150, y = 250)

hfects_entry_6 = placeholder_entry(root, "ECTS", width = 15)
hfects_entry_6.place(x = 150, y = 275)

#Berechnung Modul 7

title_1_7 = Label(root, text = "Modul 7: ")
title_1_7.place(x = 250, y = 75)

hfn_entry_7 = placeholder_entry(root, "Note", width = 15)
hfn_entry_7.place(x = 250, y = 100)

hfects_entry_7 = placeholder_entry(root, "ECTS", width = 15)
hfects_entry_7.place(x = 250, y = 125)

#Berechnung Modul 8

title_1_8 = Label(root, text = "Modul 8: ")
title_1_8.place(x = 250, y = 150)

hfn_entry_8 = placeholder_entry(root, "Note", width = 15)
hfn_entry_8.place(x = 250, y = 175)

hfects_entry_8 = placeholder_entry(root, "ECTS", width = 15)
hfects_entry_8.place(x = 250, y = 200)

#Berechnung Modul 9

title_1_9 = Label(root, text = "Modul 9: ")
title_1_9.place(x = 250, y = 225)

hfn_entry_9 = placeholder_entry(root, "Note", width = 15)
hfn_entry_9.place(x = 250, y = 250)

hfects_entry_9 = placeholder_entry(root, "ECTS", width = 15)
hfects_entry_9.place(x = 250, y = 275)

#Berechnung Modul 10

title_1_10 = Label(root, text = "Modul 10: ")
title_1_10.place(x = 350, y = 75)

hfn_entry_10 = placeholder_entry(root, "Note", width = 15)
hfn_entry_10.place(x = 350, y = 100)

hfects_entry_10 = placeholder_entry(root, "ECTS", width = 15)
hfects_entry_10.place(x = 350, y = 125)

#Berechnung Modul 11

title_1_11 = Label(root, text = "Modul 11: ")
title_1_11.place(x = 350, y = 150)

hfn_entry_11 = placeholder_entry(root, "Note", width = 15)
hfn_entry_11.place(x = 350, y = 175)

hfects_entry_11 = placeholder_entry(root, "ECTS", width = 15)
hfects_entry_11.place(x = 350, y = 200)

#Berechnung Modul 12

title_1_12 = Label(root, text = "Modul 12: ")
title_1_12.place(x = 350, y = 225)

hfn_entry_12 = placeholder_entry(root, "Note", width = 15)
hfn_entry_12.place(x = 350, y = 250)

hfects_entry_12 = placeholder_entry(root, "ECTS", width = 15)
hfects_entry_12.place(x = 350, y = 275)

#Berechnung Bachelormodul

title_1_13 = Label(root, text = "Bachelormodul: ")
title_1_13.place(x = 450, y = 75)

hfn_entry_13 = placeholder_entry(root, "Note", width = 15)
hfn_entry_13.place(x = 450, y = 100)

hfects_entry_13 = placeholder_entry(root, "ECTS", width = 15)
hfects_entry_13.place(x = 450, y = 125)

#Nebenfach

title_2 = Label(root, text = "Nebenfach: ")
title_2.place(x = 50, y = 315)

#Berechnung Modul 1

title_2_1 = Label(root, text = "Modul 1: ")
title_2_1.place(x = 50, y = 350)

nfn_entry_1 = placeholder_entry(root, "Note", width = 15)
nfn_entry_1.place(x = 50, y = 375)

nfects_entry_1 = placeholder_entry(root, "ECTS", width = 15)
nfects_entry_1.place(x = 50, y = 400)

#Berechnung Modul 2

title_2_2 = Label(root, text = "Modul 2: ")
title_2_2.place(x = 50, y = 425)

nfn_entry_2 = placeholder_entry(root, "Note", width = 15)
nfn_entry_2.place(x = 50, y = 450)

nfects_entry_2 = placeholder_entry(root, "ECTS", width = 15)
nfects_entry_2.place(x = 50, y = 475)

#Berechnung Modul 3

title_2_3 = Label(root, text = "Modul 3: ")
title_2_3.place(x = 50, y = 500)

nfn_entry_3 = placeholder_entry(root, "Note", width = 15)
nfn_entry_3.place(x = 50, y = 525)

nfects_entry_3 = placeholder_entry(root, "ECTS", width = 15)
nfects_entry_3.place(x = 50, y = 550)

#Berechnung Modul 4

title_2_4 = Label(root, text = "Modul 4: ")
title_2_4.place(x = 150, y = 350)

nfn_entry_4 = placeholder_entry(root, "Note", width = 15)
nfn_entry_4.place(x = 150, y = 375)

nfects_entry_4 = placeholder_entry(root, "ECTS", width = 15)
nfects_entry_4.place(x = 150, y = 400)

#Berechnung Modul 5

title_2_5 = Label(root, text = "Modul 5: ")
title_2_5.place(x = 150, y = 425)

nfn_entry_5 = placeholder_entry(root, "Note", width = 15)
nfn_entry_5.place(x = 150, y = 450)

nfects_entry_5 = placeholder_entry(root, "ECTS", width = 15)
nfects_entry_5.place(x = 150, y = 475)

#Berechnung Modul 6

title_2_6 = Label(root, text = "Modul 6: ")
title_2_6.place(x = 150, y = 500)

nfn_entry_6 = placeholder_entry(root, "Note", width = 15)
nfn_entry_6.place(x = 150, y = 525)

nfects_entry_6 = placeholder_entry(root, "ECTS", width = 15)
nfects_entry_6.place(x = 150, y = 550)

#Berechnung Modul 7

title_2_7 = Label(root, text = "Modul 7: ")
title_2_7.place(x = 250, y = 350)

nfn_entry_7 = placeholder_entry(root, "Note", width = 15)
nfn_entry_7.place(x = 250, y = 375)

nfects_entry_7 = placeholder_entry(root, "ECTS", width = 15)
nfects_entry_7.place(x = 250, y = 400)

#Berechnung Modul 8

title_2_8 = Label(root, text = "Modul 8: ")
title_2_8.place(x = 250, y = 425)

nfn_entry_8 = placeholder_entry(root, "Note", width = 15)
nfn_entry_8.place(x = 250, y = 450)

nfects_entry_8 = placeholder_entry(root, "ECTS", width = 15)
nfects_entry_8.place(x = 250, y = 475)

#Berechung Modul 9

title_2_9 = Label(root, text = "Modul 9: ")
title_2_9.place(x = 250, y = 500)

nfn_entry_9 = placeholder_entry(root, "Note", width = 15)
nfn_entry_9.place(x = 250, y = 525)

nfects_entry_9 = placeholder_entry(root, "ECTS", width = 15)
nfects_entry_9.place(x = 250, y = 550)

#Berechung Modul 10

title_2_10 = Label(root, text = "Modul 10: ")
title_2_10.place(x = 350, y = 350)

nfn_entry_10 = placeholder_entry(root, "Note", width = 15)
nfn_entry_10.place(x = 350, y = 375)

nfects_entry_10 = placeholder_entry(root, "ECTS", width = 15)
nfects_entry_10.place(x = 350, y = 400)


gradeslist = [hfn_entry_1, hfn_entry_2, hfn_entry_3, hfn_entry_4, hfn_entry_5, hfn_entry_6, hfn_entry_7, hfn_entry_8, hfn_entry_9, hfn_entry_10, hfn_entry_11, hfn_entry_12, hfn_entry_13, nfn_entry_1, nfn_entry_2, nfn_entry_3, nfn_entry_4, nfn_entry_5, nfn_entry_6, nfn_entry_7, nfn_entry_8, nfn_entry_9, nfn_entry_10]
ectslist = [hfects_entry_1, hfects_entry_2, hfects_entry_3, hfects_entry_4, hfects_entry_5, hfects_entry_6, hfects_entry_7, hfects_entry_8, hfects_entry_9, hfects_entry_10, hfects_entry_11, hfects_entry_12, hfects_entry_13, nfects_entry_1, nfects_entry_2, nfects_entry_3, nfects_entry_4, nfects_entry_5, nfects_entry_6, nfects_entry_7, nfects_entry_8, nfects_entry_9, nfects_entry_10]


def grade_calculation():
    grades_combined = float(hfn_entry_1.get()) * float(hfects_entry_1.get()) + float(hfn_entry_2.get()) * float(hfects_entry_2.get()) + float(hfn_entry_3.get()) * float(hfects_entry_3.get()) + float(hfn_entry_4.get()) * float(hfects_entry_4.get()) + float(hfn_entry_5.get()) * float(hfects_entry_5.get()) + float(hfn_entry_6.get()) * float(hfects_entry_6.get()) + float(hfn_entry_7.get()) * float(hfects_entry_7.get()) + float(hfn_entry_8.get()) * float(hfects_entry_8.get()) + float(hfn_entry_9.get()) * float(hfects_entry_9.get()) + float(hfn_entry_10.get()) * float(hfects_entry_10.get()) + float(hfn_entry_11.get()) * float(hfects_entry_11.get()) + float(hfn_entry_12.get()) * float(hfects_entry_12.get()) + float(hfn_entry_13.get()) * float(hfects_entry_13.get()) + float(nfn_entry_1.get()) * float(nfects_entry_1.get()) + float(nfn_entry_2.get()) * float(nfects_entry_2.get()) + float(nfn_entry_3.get()) * float(nfects_entry_3.get()) + float(nfn_entry_4.get()) * float(nfects_entry_4.get()) + float(nfn_entry_5.get()) * float(nfects_entry_5.get()) + float(nfn_entry_6.get()) * float(nfects_entry_6.get()) + float(nfn_entry_7.get()) * float(nfects_entry_7.get()) + float(nfn_entry_8.get()) * float(nfects_entry_8.get()) + float(nfn_entry_9.get()) * float(nfects_entry_9.get()) + float(nfn_entry_10.get()) * float(nfects_entry_10.get())
    ects_combined = float(hfects_entry_1.get()) + float(hfects_entry_2.get()) + float(hfects_entry_3.get()) + float(hfects_entry_4.get()) + float(hfects_entry_5.get()) + float(hfects_entry_6.get()) + float(hfects_entry_7.get()) + float(hfects_entry_8.get()) + float(hfects_entry_9.get()) + float(hfects_entry_10.get()) + float(hfects_entry_11.get()) + float(hfects_entry_12.get()) + float(hfects_entry_13.get()) + float(nfects_entry_1.get()) + float(nfects_entry_2.get()) + float(nfects_entry_3.get()) + float(nfects_entry_4.get()) + float(nfects_entry_5.get()) + float(nfects_entry_6.get()) + float(nfects_entry_7.get()) + float(nfects_entry_8.get()) + float(nfects_entry_9.get()) + float(nfects_entry_10.get())
    finalgrade = "{:.2f}".format(grades_combined / ects_combined)
    finalgradeoutput = Label(root, text = str(finalgrade))
    finalgradeoutput.place(x = 445, y = 630)

def hf_grade_calculation():
    hf_grades_combined = float(hfn_entry_1.get()) * float(hfects_entry_1.get()) + float(hfn_entry_2.get()) * float(hfects_entry_2.get()) + float(hfn_entry_3.get()) * float(hfects_entry_3.get()) + float(hfn_entry_4.get()) * float(hfects_entry_4.get()) + float(hfn_entry_5.get()) * float(hfects_entry_5.get()) + float(hfn_entry_6.get()) * float(hfects_entry_6.get()) + float(hfn_entry_7.get()) * float(hfects_entry_7.get()) + float(hfn_entry_8.get()) * float(hfects_entry_8.get()) + float(hfn_entry_9.get()) * float(hfects_entry_9.get()) + float(hfn_entry_10.get()) * float(hfects_entry_10.get()) + float(hfn_entry_11.get()) * float(hfects_entry_11.get()) + float(hfn_entry_12.get()) * float(hfects_entry_12.get()) + float(hfn_entry_13.get()) * float(hfects_entry_13.get())
    hf_ects_combined = float(hfects_entry_1.get()) + float(hfects_entry_2.get()) + float(hfects_entry_3.get()) + float(hfects_entry_4.get()) + float(hfects_entry_5.get()) + float(hfects_entry_6.get()) + float(hfects_entry_7.get()) + float(hfects_entry_8.get()) + float(hfects_entry_9.get()) + float(hfects_entry_10.get()) + float(hfects_entry_11.get()) + float(hfects_entry_12.get()) + float(hfects_entry_13.get())
    hfgrade = "{:.2f}".format(hf_grades_combined / hf_ects_combined)
    hfgradeoutput = Label(root, text = str(hfgrade))
    hfgradeoutput.place(x = 665, y = 160)

def nf_grade_calculation():
    nf_grades_combined = float(nfn_entry_1.get()) * float(nfects_entry_1.get()) + float(nfn_entry_2.get()) * float(nfects_entry_2.get()) + float(nfn_entry_3.get()) * float(nfects_entry_3.get()) + float(nfn_entry_4.get()) * float(nfects_entry_4.get()) + float(nfn_entry_5.get()) * float(nfects_entry_5.get()) + float(nfn_entry_6.get()) * float(nfects_entry_6.get()) + float(nfn_entry_7.get()) * float(nfects_entry_7.get()) + float(nfn_entry_8.get()) * float(nfects_entry_8.get()) + float(nfn_entry_9.get()) * float(nfects_entry_9.get()) + float(nfn_entry_10.get()) * float(nfects_entry_10.get())
    nf_ects_combined = float(nfects_entry_1.get()) + float(nfects_entry_2.get()) + float(nfects_entry_3.get()) + float(nfects_entry_4.get()) + float(nfects_entry_5.get()) + float(nfects_entry_6.get()) + float(nfects_entry_7.get()) + float(nfects_entry_8.get()) + float(nfects_entry_9.get()) + float(nfects_entry_10.get())
    nfgrade = "{:.2f}".format(nf_grades_combined / nf_ects_combined)
    nfgradeoutput = Label(root, text = str(nfgrade))
    nfgradeoutput.place(x = 665, y = 385 )

#Note Hauptfach Anzeige

hfgradepredisplay = Label(root, text = "Note Hauptfach: ")
hfgradepredisplay.place(x = 570, y = 160)

#Note Nebenfach Anzeige

nfgradepredisplay = Label(root, text = "Note Nebenfach: ")
nfgradepredisplay.place(x = 570, y = 385)

#Gesamtnote Anzeige

finalgradepredisplay = Label(root, text = "Gesamtnote: ")
finalgradepredisplay.place(x = 350, y = 615)

#Buttons

hf_calculation_button = Button(root, text = "Berechnung Hauptfach", command = hf_grade_calculation, borderwidth = 5)
hf_calculation_button.place(x = 570, y = 125)

nf_calculation_button = Button(root, text = "Berechnung Nebenfach", command = nf_grade_calculation, borderwidth = 5)
nf_calculation_button.place(x = 570, y = 350)

calculate_button = Button(root, text = "Gesamtnote berechnen", command = grade_calculation, borderwidth = 5)
calculate_button.place(x = 350, y = 580)

root.mainloop()
