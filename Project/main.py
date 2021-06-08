import tkinter as tk
import tkinter.font as font

window = tk.Tk()
window.title("Mortgage Calculator")
window.geometry("350x600")

Title = tk.Label(window,text="Calculate Mortgage", font=("Arial", 17), foreground="red").pack(padx=10, pady=10)

tk.Label(window, text="Input 1", font=("Arial", 12)).pack(padx=10, pady=10)
e1 = tk.Entry(window)
e1.pack()

tk.Label(window, text="Input 2", font=("Arial", 12)).pack(padx=10, pady=10)
e2 = tk.Entry(window)
e2.pack()

window.mainloop()