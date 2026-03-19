from customtkinter import *

launcher = CTk()
launcher.geometry("400x500")
launcher.title("Agario Launcher")

heading = CTkLabel(launcher,text="AGARGARIO",font=("Arial",30,'bold'))
heading.pack(pady=15)

row1=CTkFrame(launcher,height=75)
name_label = CTkLabel(row1, text="Ваш нікнейм",anchor='w')
name_entry = CTkEntry(row1, placeholder_text="Нікнейм...")

name_label.pack(fill='x',padx=5)
name_entry.pack(fill='x',padx=5)

row2=CTkFrame(launcher,height=75)
host_label = CTkLabel(row2, text="IP серверу",anchor='w')
host_entry = CTkEntry(row2, placeholder_text="IP...")

host_label.pack(fill='x',padx=5)
host_entry.pack(fill='x',padx=5)

row3=CTkFrame(launcher,height=75)
port_label = CTkLabel(row3, text="PORT серверу",anchor='w')
port_entry = CTkEntry(row3, placeholder_text="PORT...")

port_label.pack(fill='x',padx=5)
port_entry.pack(fill='x',padx=5)

row1.pack(pady=20, fill='x',padx=15)
row1.pack_propagate(False)
row2.pack(pady=20, fill='x',padx=15)
row2.pack_propagate(False)
row3.pack(pady=20, fill='x',padx=15)
row3.pack_propagate(False)

connect_btn = CTkButton(launcher, text="Під'єднатись")
connect_btn.pack(pady=15)

launcher.mainloop()