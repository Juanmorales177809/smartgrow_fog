import os, json
from tkinter import *
import time

root = Tk()
root.resizable(False,False)
url = "192.168.1.128"
cmd="curl -s -k " + url
print (cmd)

variable_control = StringVar()
variable_control_hora = StringVar()

def actualizar_hora():
    hora = time.strftime("%H:%M:%S")
    variable_control_hora.set(hora)
    root.after(1000,actualizar_hora)
def actualizar():
    result = os.popen(cmd).read()
    arr = json.loads(result)
    variable_control.set(arr['variables']['temp']/100)
    root.after(1000,actualizar)
    

#temp['variables']['temp']/100
reloj = Label(root,textvariable=variable_control_hora,fg='blue',font=('Arial',25),padx=40,pady=20)
reloj.pack()
label = Label(root,textvariable= variable_control,fg='red',font=('Arial',25),padx=20,pady=20)
label.pack()
actualizar_hora()
actualizar()
root.mainloop()
