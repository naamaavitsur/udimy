from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(400, 200)
window.config(padx=30, pady=30)

def buttom_clicked():
    the_mile_to_convert = mile_input.get()
    km_calculte = float(the_mile_to_convert)*1.609344
    calculated_to_km.config(text=km_calculte)


mile_input = Entry(width=5, font=("Ariel", 20))
mile_input.insert(END, string="0")
mile_input.grid(column=1, row=0)

mile_label = Label(text="Miles", font=("Ariel", 20))
mile_label.grid(column=2, row=0)

is_equel_label = Label(text="is equal to", font=("Ariel", 20))
is_equel_label.grid(column=0, row=1)

calculated_to_km = Label(text="0", font=("Ariel", 20))
calculated_to_km.grid(column=1, row=1)

km_label = Label(text="Km", font=("Ariel", 20))
km_label.grid(column=2, row=1)

calculat_button = Button(text="Calculate", command=buttom_clicked)
calculat_button.grid(column=1, row=3)








window.mainloop()
