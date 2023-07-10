import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

2.	El departamento de Construcción Rural requiere una herramienta que facilite el calculo de materiales necesarios 
a la hora de realizar un alambrado permetral, se le solicita al usuario que ingrese el ancho y el largo del terreno.

    A. Informar los metros cuadrados del terreno y los metros lineales del perimetro
    B. Informar la cantidad de postes de quebracho Grueso de 2.4 mts (van cada 250 mts lineales y en las esquinas).
    C. Informar la cantidad de postes de quebracho Fino de 2.2 mts (van cada 12 mts lineales, si en su lugar no se encuentra el poste grueso).
    D. Informar la cantidad de varillas (van cada 2 mts lineales).
    E. Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos.

    EJ 36 MTS X 24 MTS 
    (G)Poste Quebracho Grueso de 2.4 mts
    (F)Poste Quebracho Fino de 2.2 mts
    (V)Varillas
    
    G V V V V V F V V V V V F V V V V V G
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    F                                   F
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    G V V V V V F V V V V V F V V V V V G
    
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Largo")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_largo = customtkinter.CTkEntry(master=self)
        self.txt_largo.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Ancho")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)

        self.txt_ancho = customtkinter.CTkEntry(master=self)
        self.txt_ancho.grid(row=1, column=1)

        self.btn_calcular = customtkinter.CTkButton(
            master=self, text="CALCULAR", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")

    def btn_calcular_on_click(self):
       # A. 
        
        largo_terreno = self.txt_largo.get()
        largo_terreno_num = int(largo_terreno)
        
        ancho_terreno = self.txt_ancho.get()
        ancho_terreno_num = int(ancho_terreno)

        metros_cuadrados = (largo_terreno_num * ancho_terreno_num)

        metros_lineales = (largo_terreno_num + ancho_terreno_num) * 2

        mensaje_a= f"Metros Cuadrados: {metros_cuadrados}\nMetros Lineales: {metros_lineales}"
       
        alert("Metros Cuadrados del Terreno", mensaje_a)

        # B.  

        cantidad_quebracho_grueso = 4 + (metros_lineales // 250)

        mensaje_b = f"Cantidad de postes gruesos: {cantidad_quebracho_grueso}"
        
        alert("Punto B", mensaje_b)



        # C. 

        cantidad_quebracho_fino = (metros_lineales // 12 - cantidad_quebracho_grueso)

        mensaje_c = f"Cantidad de postes finos: {cantidad_quebracho_fino}"

        alert("Punto C", mensaje_c)

        # D.

        varillas = (metros_lineales // 2 - cantidad_quebracho_grueso - cantidad_quebracho_fino)

        mensaje_d = f"Cantidad de varillas: {varillas}"

        alert("Punto D", mensaje_d)

        # E.

        alambre = (metros_lineales * 7)

        mensaje_e = f"Cantidad Alambre: {alambre}"

        alert("Punto E", mensaje_e)

        



       
        
        








if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
