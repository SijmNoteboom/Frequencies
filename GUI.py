import tkinter as tk

# GUI general setup
win = tk.Tk()

win.title('Sound Generator')
win.geometry("1200x700+200+50")

Label_Hz = tk.Label(win, text='Frequency:').grid(row=0)
frequency_input = tk.Entry(win, width=10)
frequency_input.grid(column=1, row=0)
Button_ok = tk.Button(win, text='OK').grid(row=0)


win.mainloop()
