import tkinter as tk

window = tk.Tk()# Crear la ventana
window.title("Gestión de Pacientes")# Titulo de la ventana


# Parte 1 (BST): Gestionar los registros de pacientes por número de expediente, 
# permitiendo agregar, buscar y eliminar registros. 
# Crear una interfaz para que los usuarios puedan agregar, buscar y eliminar registros de pacientes.

# Funcion para agregar registros de pacientes
def agregar():
    return 0
# Funcion para buscar registros de pacientes    
def buscar():
    return 0    
# Funcion para eliminar registros de pacientes
def eliminar():
    return 0

# Parte 2 (AVL): Mantener la lista de doctores con inserciones y búsquedas rápidas. 
# La interfaz debe permitir a los usuarios ver, agregar y buscar doctores.
# Funcion para ver la lista de doctores
def ver_doctores():
    return 0
# Funcion para agregar doctores
def agregar_doctores():
    return 0
# Funcion para buscar doctores
def buscar_doctores():
    return 0

# Parte 3 (Grafo): Modelar la red de hospitales y encontrar la ruta más corta para la transferencia de pacientes. 
# La interfaz debe permitir a los usuarios calcular y gestionar las transferencias de pacientes entre hospitales.
# Funcion para calcular la ruta más corta
def calcular_ruta():
    return 0
# Funcion para gestionar las transferencias
def gestionar_transferencias():
    return 0

    

    
altura_window = 900 # Altura de la ventana
ancho_window = 1440 # Ancho de la ventana
window.geometry(f"{ancho_window}x{altura_window}")# Tamaño de la ventana


#Botones comentados ya que no se han implementado las funciones correctamente ni el diseño final

#btn_close = tk.Button(window, text="Cerrar", command=window.quit)# Crear un boton para cerrar la ventana
#btn_close.pack()# Agregar el boton a la ventana
#btn_close.place(x=ancho_window/2, y=altura_window-50)# Posicionar el boton

#btn_retro = tk.Button(window, text="Retroceder", command=retro)# Crear un boton para cerrar la ventana
#btn_retro.pack()# Agregar el boton a la ventana
#btn_retro.place(x=ancho_window/2-100, y=altura_window-50)# Posicionar el boton

#btn_avanz = tk.Button(window, text="Avanzar", command=siguiente)# Crear un boton para cerrar la ventana
#btn_avanz.pack()# Agregar el boton a la ventana
#btn_avanz.place(x=ancho_window/2+100, y=altura_window-50)# Posicionar el boton

window.mainloop()# Mostrar la ventana, este es comentario propio -> el mainloop hace que se cree un loop infinito para que la ventana se mantenga abierta, 
                 # ya que tengo entendido que sin el mainloop el programa se cierra en el mismo momento en el que se abre.

