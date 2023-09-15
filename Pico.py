from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

def crackcmd(keys = {"Windows 10 Home": "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99", "Windows 10 Home N": "3KHY7-WNT83-DGQKR-F7HPR-844BM", "Windows 10 Home Single Language": "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH","Windows 10 Home Country Specific": "PVMJN-6DFY6-9CCP6-7BKTT-D3WVR","Windows 10 Professional": "W269N-WFGWX-YVC9B-4J6C9-T83GX","Windows 10 Professional N": "MH37W-N47XK-V7XM9-C7227-GCQG9","Windows 10 Enterprise": "NPPR9-FWDCX-D2C8J-H872K-2YT43","Windows 10 Enterprise N": "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4","Windows 10 Education": "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2","Windows 10 Education N": "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ","Windows 10 Enterprise 2015 LTSB": "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99","Windows 10 Enterprise 2015 LTSB N": "2F77B-TNFGY-69QQF-B8YKP-D69TJ",}):
    ver = winVer.get()
    if ver != 'Selecciona' and messagebox.askyesno("", f"Estás a punto de crackear windows: \n{ver} \n\n¿Correcto?"):
        try:
            print("slmgr /skms kms.digiboy.ir")
            print("slmgr /ato")
            print(f"slmgr /ipk {keys[ver]}")
        except KeyError as ex:
            messagebox.showerror("Error", "Selecciona una versión válida")
            print(ex)

values = ["Windows 10 Home","Windows 10 Home N", "Windows 10 Home Single Language", "Windows 10 Home Country Specific", "Windows 10 Professional","Windows 10 Professional N","Windows 10 Enterprise","Windows 10 Enterprise N","Windows 10 Education","Windows 10 Education N","Windows 10 Enterprise 2015 LTSB","Windows 10 Enterprise 2015 LTSB N",]

root = Tk()
root.resizable(0,0)
root.title("Dewa's Pico")
root.geometry("250x120")
root.iconbitmap("icon.ico")

title = Label(
    root,
    text="Welcome to Dewa's Pico",
    font="Arial, 15",
    pady=10
).pack()

select = Label(
    root,
    text="Selecciona tu versión de windows:",
).pack()

winVer = ttk.Combobox(
    root,
    values=values,
    width=35
)
winVer.pack()
winVer.set("Selecciona")

crack = Button(
    root,
    command=crackcmd,
    text="Crack",
    pady=4
).pack()

root.mainloop()