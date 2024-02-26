import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

Caloption = "Voltage"

Voltage = 10
Current = 5
Resistance = 0

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('415x280')
        self.root.title('Ohm\'s law calculator')
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)

        self.text = tk.Label(self.mainframe, text='Answer goes here', background='white', font=("Brass Mono", 30))
        self.text.grid(row=0, column=0)

        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0, pady=10, sticky='NWES')
        set_text_button = ttk.Button(self.mainframe, text='Set Voltage', command=self.set_voltage)
        set_text_button.grid(row=1, column=1, pady=10)

        self.set_current_field = ttk.Entry(self.mainframe)
        self.set_current_field.grid(row=2, column=0, pady=10, sticky='NWES')
        set_current_button = ttk.Button(self.mainframe, text='Set Current', command=self.set_current)
        set_current_button.grid(row=2, column=1, pady=10)

        self.set_resistance_field = ttk.Entry(self.mainframe)
        self.set_resistance_field.grid(row=3, column=0, pady=10, sticky='NWES')
        set_resistance_button = ttk.Button(self.mainframe, text='Set Resistance', command=self.set_resistance)
        set_resistance_button.grid(row=3, column=1, pady=10)

        cal_options = ['Voltage', 'Current', 'Resistance']
        self.set_cal_field = ttk.Combobox(self.mainframe, values=cal_options)
        self.set_cal_field.grid(row=4, column=0, sticky='NWES', pady=10)
        set_cal_button = ttk.Button(self.mainframe, text='Set Option', command=self.set_option)
        set_cal_button.grid(row=4, column=1, pady=10)

        set_answer_button = ttk.Button(self.mainframe, text='Calculate', command=self.set_answer)
        set_answer_button.grid(row=5, column=0, pady=10, sticky='NWES')

        self.root.mainloop()
        return

    def set_voltage(self):
        if self.set_text_field.get():
            newvoltage = self.set_text_field.get()
            global Voltage
            Voltage = newvoltage
            print(Voltage)
        else:
            messagebox.showerror('Value Error', 'Your value is empty.')

    def set_current(self):
        if self.set_current_field.get():
            newcurrent = self.set_current_field.get()
            global Current
            Current = newcurrent
            print(Current)
        else:
            messagebox.showerror('Value Error', 'Your value is empty.')

    def set_resistance(self):
        if self.set_resistance_field.get():
            newresistance = self.set_resistance_field.get()
            global Resistance
            Resistance = newresistance
            print(Resistance)
        else:
            messagebox.showerror('Value Error', 'Your value is empty.')

    def set_answer(self):
        global Voltage
        global Current
        global Resistance
        if Caloption == "Voltage":
            print(Voltage)
            print(Current)
            print(Resistance)
            Voltage = int(Current) * int(Resistance)
            self.text.config(text=str(Current) + " A x " + str(Resistance) + " Ω = " + str(round(Voltage, 2)) + " V")
        elif Caloption == "Current":
            if int(Voltage) or int(Resistance) != 0:
                Current = int(Voltage) / int(Resistance)
                self.text.config(text=str(Voltage) + " V / " + str(Resistance) + " Ω = " + str(round(Current, 2)) + " A")
            else:
                messagebox.showerror('Division Error', 'You can not divide a number by zero. Check your values.')
        elif Caloption == "Resistance":
            if int(Voltage) or int(Current) != 0:
                Resistance = int(Voltage) / int(Current)
                self.text.config(text=str(Voltage) + " V / " + str(Current) + " A = " + str(round(Resistance, 2)) + " Ω")
            else:
                messagebox.showerror('Division Error', 'You can not divide a number by zero. Check your values.')
        # newtext = self.set_text_field.get()
        # self.text.config(text=newtext)

    def set_option(self):
        global Caloption
        if self.set_cal_field.get():
            newoption = self.set_cal_field.get()
            Caloption = newoption
            print(Caloption)
        else:
            messagebox.showerror('Value Error', 'Your value is empty.')

if __name__ == '__main__':
    App()
