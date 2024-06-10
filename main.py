# Catalina Fonseca, Carlos Huenuman, Pamela Vielma
import tkinter as tk
from tkinter import ttk, messagebox
from Bst import BST
from avl import ArbolAVL
from Grafos import Grafos

window = tk.Tk() # Crear la ventana
window.title("Sistema de Gestión de Pacientes") # Titulo de la ventana
altura_window = 480 # Altura de la ventana
ancho_window = 1130 # Ancho de la ventana
window.geometry(f"{ancho_window}x{altura_window}") # Tamaño de la ventana

# Parte 1 Elementos Tkinter
# Etiqueta y campo de entrada para el nombre del paciente
label_nombre = tk.Label(window, text="Nombre del Paciente:")
label_nombre.grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(window)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

# Etiqueta y campo de entrada para el número de expediente
label_expediente = tk.Label(window, text="Número de Expediente:")
label_expediente.grid(row=1, column=0, padx=10, pady=5)
entry_expediente = tk.Entry(window)
entry_expediente.grid(row=1, column=1, padx=10, pady=5)
# Crear una tabla para mostrar registros de pacientes
treeview = ttk.Treeview(window, columns=('Nombre', 'Expediente'))
treeview.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
treeview.column('#0', width=0, stretch=tk.NO)
treeview.heading('Nombre', text='Nombre del Paciente')
treeview.heading('Expediente', text='Número de Expediente')

# Crear un objeto de la clase BST
arbol_pacientes = BST()

#Parte 2 Elementos Tkinter
# Etiqueta y campo de entrada para el nombre del doctor
label_doctor = tk.Label(window, text="Nombre del Doctor:")
label_doctor.grid(row=0, column=2, padx=10, pady=5)
entry_doctor = tk.Entry(window)
entry_doctor.grid(row=0, column=3, padx=10, pady=5)

label_id = tk.Label(window, text="ID:")
label_id.grid(row=1, column=2, padx=10, pady=5)
entry_id = tk.Entry(window)
entry_id.grid(row=1, column=3, padx=10, pady=5)

# Crear una tabla para mostrar registros de doctores
treeview_doctores = ttk.Treeview(window, columns=('Nombre', 'ID'))
treeview_doctores.grid(row=5, column=2, columnspan=2, padx=10, pady=5)
treeview_doctores.column('#0', width=0, stretch=tk.NO)
treeview_doctores.heading('Nombre', text='Nombre del Doctor')
treeview_doctores.heading('ID', text='ID')

arbol_avl = ArbolAVL()



#Parte 3 Elementos 
# Etiqueta y campo de entrada para el hospital de origen
label_origen = tk.Label(window, text="Hospital de Origen:")
label_origen.grid(row=0, column=4, padx=10, pady=5)
entry_hospital_origen = tk.Entry(window)
entry_hospital_origen.grid(row=0, column=5, padx=10, pady=5)

# Etiqueta y campo de entrada para el hospital de destino
label_destino = tk.Label(window, text="Hospital de Destino:")
label_destino.grid(row=1, column=4, padx=10, pady=5)
entry_hospital_destino = tk.Entry(window)
entry_hospital_destino.grid(row=1, column=5, padx=10, pady=5)
# Etiqueta y campo de entrada para el nombre del paciente
label_nombre_transf = tk.Label(window, text="Nombre del Paciente:")
label_nombre_transf.grid(row=2, column=4, padx=10, pady=5)
entry_nombre_transf = tk.Entry(window)
entry_nombre_transf.grid(row=2, column=5, padx=10, pady=5)

grafo = Grafos()



#Parte 1 (BST): Gestionar los registros de pacientes por número de expediente, 
#Permitiendo agregar, buscar y eliminar registros. 
#Crear una interfaz para que los usuarios puedan agregar, buscar y eliminar registros de pacientes.
def agregar():
    if not entry_expediente.get() or not entry_nombre.get():
            messagebox.showerror("Error", "Por favor, complete los campos necesarios: Nombre de Paciente y Numero de Expediente.")
            return
    try:
        nombre = entry_nombre.get()
        expediente = int(entry_expediente.get())
        arbol_pacientes.Agregar(expediente, nombre)
        actualizar_tabla()
        entry_expediente.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número de expediente válido.")
        return

def buscar():
    expediente = int(entry_expediente.get())
    paciente = arbol_pacientes.Buscar(expediente)
    if paciente:
        messagebox.showinfo("Resultado de Búsqueda", f"Paciente encontrado: {paciente}")
    else:
        messagebox.showinfo("Resultado de Búsqueda", "Paciente no encontrado")

def eliminar():
    expediente = int(entry_expediente.get())
    arbol_pacientes.Eliminar(expediente)
    messagebox.showinfo("Eliminación de Registro", "Registro eliminado correctamente")
    actualizar_tabla()
    
def actualizar_tabla():
    # Limpiar la tabla
    for row in treeview.get_children():
        treeview.delete(row)
    # Rellenar la tabla con datos del árbol BST
    _rellenar_tabla(arbol_pacientes.Raiz)

def _rellenar_tabla(nodo):
    if nodo:# Insertar el nodo actual en la tabla y continuar con los nodos izquierdo y derecho
        treeview.insert('', 'end', text=str(id(nodo)), values=(nodo.Nombre, nodo.Expediente))
        _rellenar_tabla(nodo.Izquierda)# Llamada recursiva para el nodo izquierdo
        _rellenar_tabla(nodo.Derecha)#  Llamada recursiva para el nodo derecho

#Parte 2 (AVL): Mantener la lista de doctores con inserciones y búsquedas rápidas. 
#La interfaz debe permitir a los usuarios ver, agregar y buscar doctores.
def agregar_doctor():
        # Validar que los campos de entrada no estén vacíos
        if not entry_id.get() or not entry_doctor.get():
            messagebox.showerror("Error", "Por favor, los campos necesarios: Nombre del Doctor y ID.")
            return

        try:# Obtener la clave y el nombre del doctor
            clave = int(entry_id.get())
            nombre = entry_doctor.get()
            # Agregar un doctor al árbol AVL
            arbol_avl.raiz = arbol_avl.insertar(arbol_avl.raiz, clave, nombre)
            # Actualizar la interfaz para reflejar los cambios
            actualizar_lista_doctores()
            # Limpiar los campos de entrada después de agregar
            entry_id.delete(0, tk.END)
            entry_doctor.delete(0, tk.END)
        except ValueError:# Manejar errores de tipo de datos
            print("La clave debe ser un número entero.")

def buscar_doctor():
        # Validar que el campo de búsqueda no esté vacío
        if not entry_id.get():
            print("Por favor, ingrese la clave del doctor a buscar.")
            return

        try:
            clave = int(entry_id.get())# Obtener la clave del doctor a buscar
            # Buscar el doctor en el árbol AVL
            doctor =(arbol_avl.buscar(arbol_avl.raiz, clave))
            if doctor:
                # Si se encuentra, mostrar la información del doctor en la interfaz
                #print(f"Doctor encontrado - Clave: {doctor.clave}, Nombre: {doctor.nombre}")
                messagebox.showinfo("Resultado de Búsqueda", f"EL Doctor ha sido encontrado \nID: {doctor.clave}, Nombre: {doctor.nombre}")
            else:
                print("Doctor no encontrado")
        except ValueError:
            print("La clave debe ser un número entero.")

    
def actualizar_lista_doctores():
        # Limpiar la lista de doctores
        for doctor in treeview_doctores.get_children():
            treeview_doctores.delete(doctor)

        # Obtener la lista de doctores del árbol AVL y agregarlos a la lista de Tkinter
        doctores = arbol_avl.obtener_lista_doctores()
        for doctor in doctores:
            treeview_doctores.insert("", "end", values=(doctor.nombre, doctor.clave))



#Parte 3 (Grafo): Modelar la red de hospitales y encontrar la ruta más corta para la transferencia de pacientes. 
#La interfaz debe permitir a los usuarios calcular y gestionar las transferencias de pacientes entre hospitales.
def calcular_ruta():# Función para calcular la ruta más corta entre dos hospitales
    inicio = entry_hospital_origen.get()# Obtener el hospital de origen
    fin = entry_hospital_destino.get()# Obtener el hospital de destino
    distancia_minima = grafo.Ruta_Mas_Corta(inicio, fin)# Calcular la ruta más corta
    if distancia_minima == (None, float("inf")):# Si no hay ruta disponible
        messagebox.showinfo("Ruta más corta", f"No hay una ruta disponible entre {inicio} y {fin}.")
    else: 
        messagebox.showinfo("Ruta más corta", f"La distancia mínima entre {inicio} y {fin} es de {distancia_minima[1]} km.")# Mostrar la distancia mínima en una ventana emergente

def transferir_paciente():# Función para transferir un paciente de un hospital a otro
    inicio = entry_hospital_origen.get()# Obtener el hospital de origen
    fin = entry_hospital_destino.get()# Obtener el hospital de destino
    nombre = entry_nombre_transf.get()# Obtener el nombre del paciente
    transferencia_ruta = grafo.Transferencia(inicio, fin)# Calcular la ruta de transferencia
    if transferencia_ruta == (None, float("inf")):
        messagebox.showinfo("Transferencia de Paciente", f"No hay una ruta disponible para transferir al paciente llamado: {nombre} desde {inicio} a {fin}.")
    else:
        messagebox.showinfo("Transferencia de Paciente",f" Se transfiere al paciente llamado: {nombre} \nDesde el Origen: {inicio}  al Destino: {fin}\nSiguiendo la siguiente ruta: Ruta: {' -> '.join(transferencia_ruta[0])} con una distancia de {transferencia_ruta[1]} km" )
    # Mostrar la ruta de transferencia en una ventana emergente

# Botones para agregar, buscar y eliminar registros
btn_agregar = tk.Button(window, text="Agregar Registro", command=agregar)
btn_agregar.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

btn_buscar = tk.Button(window, text="Buscar Registro", command=buscar)
btn_buscar.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

btn_eliminar = tk.Button(window, text="Eliminar Registro", command=eliminar)
btn_eliminar.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

# Botones para agregar, buscar y eliminar doctores
btn_agregar_doctor = tk.Button(window, text="Agregar Doctor", command=agregar_doctor)
btn_agregar_doctor.grid(row=3, column=2, columnspan=2, padx=10, pady=5, sticky="WE")
btn_buscar_doctor = tk.Button(window, text="Buscar Doctor", command=buscar_doctor)
btn_buscar_doctor.grid(row=4, column=2, columnspan=2, padx=10, pady=5, sticky="WE")


# Botones para calcular ruta y transferir paciente
btn_calcular_ruta = tk.Button(window, text="Calcular Ruta", command=calcular_ruta)
btn_calcular_ruta.grid(row=3, column=4, columnspan=2, padx=10, pady=5, sticky="WE")
btn_transferir_paciente = tk.Button(window, text="Transferir Paciente", command=transferir_paciente)
btn_transferir_paciente.grid(row=4, column=4, columnspan=2, padx=10, pady=5, sticky="WE")



window.mainloop() # Mostrar la ventana
# El mainloop hace que se cree un loop infinito para que la ventana se mantenga abierta, ya que tengo entendido que sin el mainloop el programa se cierra en el mismo momento en el que se abre.