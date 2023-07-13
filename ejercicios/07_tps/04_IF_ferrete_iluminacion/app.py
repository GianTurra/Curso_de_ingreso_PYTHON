import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        cantidad = self.combobox_cantidad.get()
        cantidad_num = int(cantidad)
        importe = 800
        marca = self.combobox_marca.get()
        precio_final = 0
        
        # ELSE - IF

        if(cantidad_num >= 6):
            descuento = 0.5
            precio_descuento = importe * cantidad_num * descuento 
            mensaje = "Descuento del 50% \n El total a pagar con el descuento es: {0}".format(precio_descuento)
        else:
            if(cantidad_num == 5):
                if(marca == "ArgentinaLuz"):
                    descuento = 0.4
                    precio_descuento = importe * cantidad_num * descuento
                    mensaje = "Descuento del 40% \n El total a pagar con el descuento es: {0}".format(precio_descuento)
                else:
                    descuento = 0.3
                    precio_descuento = importe * cantidad_num * descuento
                    mensaje = "Descuento del 30% \n El total a pagar con el descuento es: {0}".format(precio_descuento)
            else:        
                if(cantidad_num == 4):
                    if(marca == "ArgentinaLuz" or marca == "FelipeLamparas"):
                        descuento = 0.25
                        precio_descuento = importe * cantidad_num * descuento
                        mensaje = "Descuento del 25% \n El total a pagar con el descuento es: {0}".format(precio_descuento)
                    else:
                        descuento = 0.20
                        precio_descuento = importe * cantidad_num * descuento
                        mensaje = "Descuento del 20% \n El total a pagar con el descuento es: {0}".format(precio_descuento)
                else:
                    if(cantidad_num == 3):
                        if(marca == "ArgentinaLuz"):
                            descuento = 0.15
                            precio_descuento = importe * cantidad_num * descuento
                            mensaje = "Descuento del 15% \n El total a pagar con el descuento es: {0}".format(precio_descuento)
                        else:
                            if(marca == "FelipeLamparas"):
                                descuento = 0.10
                                precio_descuento = importe * cantidad_num * descuento
                                mensaje = "Descuento del 10% \n El total a pagar con el descuento es: {0}".format(precio_descuento)
                            else:
                                descuento = 0.05
                                precio_descuento = importe * cantidad_num * descuento
                                mensaje = "Descuento del 5% \n El total a pagar con el descuento es: {0}".format(precio_descuento)
        
        precio_descuento = importe * cantidad_num * descuento
        descuento_adicional = 0.05
        importe_final = precio_descuento - (precio_descuento * descuento_adicional)
        
        if(importe_final > 4000):
            importe_final = precio_descuento - (precio_descuento * descuento_adicional)
            mensaje = f"El total a pagar con el descuento es: {precio_descuento}\nImporte final con el descuento adicional: {importe_final:.2f}"
        
        alert("TP 4", mensaje)



        # ELIF

        if(cantidad_num >= 6):
            descuento = 0.5 
            precio_descuento = importe * cantidad_num * descuento
            mensaje = f"Descuento del 50% \n El total a pagar con el descuento es: {precio_descuento}"
        elif(cantidad_num == 5):
            if(marca == "ArgentinaLuz"):
                descuento = 0.4
                precio_descuento = importe * cantidad_num * descuento
                mensaje = f"Descuento del 40% \n El total a pagar con el descuento es: {precio_descuento}"
            else: 
                descuento = 0.3
                precio_descuento = importe * cantidad_num * descuento 
                mensaje = f"Descuento del 30% \n El total a pagar con el descuento es: {precio_descuento}"
        elif(cantidad_num == 4):
            if(marca == "ArgentinaLuz" or marca == "FelipeLamparas"):
                descuento = 0.25 
                precio_descuento = importe * cantidad_num * descuento
                mensaje = f"Descuento del 25% \n El total a pagar con el descuento es: {precio_descuento}"   
            else:
                descuento = 0.2
                precio_descuento = importe * cantidad_num * descuento 
                mensaje = f"Descuento del 20% \n El total a pagar con el descuento es: {precio_descuento}"  
        elif(cantidad_num == 3):
            if(marca == "ArgentinaLuz"):
                descuento = 0.15 
                precio_descuento = importe * cantidad_num * descuento
                mensaje = f"Descuento del 15% \n El total a pagar con el descuento es: {precio_descuento}"  
            elif(marca == "FelipeLamparas"):
                descuento = 0.10 
                precio_descuento = importe * cantidad_num * descuento
                mensaje = f"Descuento del 10% \n El total a pagar con el descuento es: {precio_descuento}"
            else:
                descuento = 0.05
                precio_descuento = importe * cantidad_num * descuento
                f"Descuento del 5% \n El total a pagar con el descuento es: {precio_descuento}"
        
        
        precio_descuento = importe * cantidad_num * descuento
        descuento_adicional = 0.05
        importe_final = precio_descuento - (precio_descuento * descuento_adicional)
        
        if(importe_final > 4000):
            importe_final = precio_descuento - (precio_descuento * descuento_adicional)
            mensaje = f"El total a pagar con el descuento es: {precio_descuento}\nImporte final con el descuento adicional: {importe_final:.2f}"
        
        alert("TP 4", mensaje)

        
        










        
        









        








    
     


            




            




        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()