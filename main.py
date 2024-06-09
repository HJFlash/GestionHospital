# Catalina Fonseca, Carlos Huenuman, Pamela Vielma
import tkinter as tk

window = tk.Tk() # Crear la ventana
window.title("Visualizador de Imagenes") # Titulo de la ventana
altura_window = 720 # Altura de la ventana
ancho_window = 1280 # Ancho de la ventana
window.geometry(f"{ancho_window}x{altura_window}") # Tamaño de la ventana

#Parte 1 (BST): Gestionar los registros de pacientes por número de expediente, 
#Permitiendo agregar, buscar y eliminar registros. 
#Crear una interfaz para que los usuarios puedan agregar, buscar y eliminar registros de pacientes.
def agregar():    
    pass
def buscar():
    pass
def eliminar():
    pass
#Parte 2 (AVL): Mantener la lista de doctores con inserciones y búsquedas rápidas. 
#La interfaz debe permitir a los usuarios ver, agregar y buscar doctores.
def agregar_doctor():
    pass
def buscar_doctor():
    pass
def eliminar_doctor():
    pass
#Parte 3 (Grafo): Modelar la red de hospitales y encontrar la ruta más corta para la transferencia de pacientes. 
#La interfaz debe permitir a los usuarios calcular y gestionar las transferencias de pacientes entre hospitales.
def calcular_ruta():
    pass
def transferir_paciente():
    pass


window.mainloop() # Mostrar la ventana

# El mainloop hace que se cree un loop infinito para que la ventana se mantenga abierta, ya que tengo entendido que sin el mainloop el programa se cierra en el mismo momento en el que se abre.