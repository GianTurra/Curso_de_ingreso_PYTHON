import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Enunciado:
Al presionar el botón ‘Pedir clave’, solicitar al usuario que ingrese una contraseña mediante prompt. 
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir, volverla a solicitar hasta que coincidan
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_pedir_clave = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_pedir_clave_on_click)
        self.btn_pedir_clave.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_pedir_clave_on_click(self):
        
        contraseña_correcta = 'utn750'
        contraseña_ingresada = None

        
        while contraseña_ingresada != contraseña_correcta:
            contraseña_ingresada = prompt("EJERCICI0 3", "Ingrese la contraseña:")

            if contraseña_ingresada == None:
                break

            if contraseña_ingresada == contraseña_correcta:
                alert("EJERCICIO 3", "Contraseña correcta")
            
            else:
                alert("EJERCICIO 3", "Contraseña incorrecta, Intente de nuevo")
                




            




      


    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()