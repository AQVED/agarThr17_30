from tkinter import PhotoImage

from customtkinter import *

class ConnectWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.title("Agario Launcher")
        self.icon = PhotoImage(file="ico_mini.png")
        self.wm_iconphoto(False, self.icon)

        self.username = None
        self.host = None
        self.port = None

        heading = CTkLabel(self, text="AGARGARIO",font=("Arial",30,'bold'))
        heading.pack(pady=15)

        row1=CTkFrame(self, height=75)
        name_label = CTkLabel(row1, text="Ваш нікнейм",anchor='w')
        self.name_entry = CTkEntry(row1, placeholder_text="Нікнейм...")

        name_label.pack(fill='x',padx=5)
        self.name_entry.pack(fill='x',padx=5)

        row2=CTkFrame(self,height=75)
        host_label = CTkLabel(row2, text="IP серверу",anchor='w')
        self.host_entry = CTkEntry(row2, placeholder_text="IP...")

        host_label.pack(fill='x',padx=5)
        self.host_entry.pack(fill='x',padx=5)

        row3=CTkFrame(self,height=75)
        port_label = CTkLabel(row3, text="PORT серверу",anchor='w')
        self.port_entry = CTkEntry(row3, placeholder_text="PORT...")

        port_label.pack(fill='x',padx=5)
        self.port_entry.pack(fill='x',padx=5)

        row1.pack(pady=20, fill='x',padx=15)
        row1.pack_propagate(False)
        row2.pack(pady=20, fill='x',padx=15)
        row2.pack_propagate(False)
        row3.pack(pady=20, fill='x',padx=15)
        row3.pack_propagate(False)

        connect_btn = CTkButton(self, text="Під'єднатись")
        connect_btn.pack(pady=15)

    def open_game(self):
        self.username = self.name_entry.get()
        self.host = self.host_entry.get()
        self.port = int(self.port_entry.get())
        self.destroy()
a=ConnectWindow()
a.mainloop()