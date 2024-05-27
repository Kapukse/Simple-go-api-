import requests, tkinter as tk
from tkinter import messagebox

def main():
    res = requests.get("http://localhost:2137/").text
    messagebox.showinfo("response", res)

gui = tk.Tk()
gui.geometry("300x200")
gui.title("client")
tk.Label(gui, text="client").pack()
tk.Button(gui, text="server response", command=main).pack()

gui.mainloop()