import tkinter as tk
def main():
     global ventana
     # Crear la ventana principal
     ventana = tk.Tk()
     ventana.geometry("400x300")
     ventana.title("Menú Centrado")
 
     # Mostrar el menú visual al inicio
     mostrarMenu()
 
     ventana.mainloop()

     if __name__=="__main__":
     main()
def mostrarMenu():
     limpiarVentana()
     label = tk.Label(ventana, text="Menú Principal", font=("Arial", 18, "bold"))
     label.pack(pady=20)
 
     boton1 = tk.Button(ventana, text="Opción 1", font=("Arial", 14), width=20, command=accion)
     boton1.pack(pady=10)
 
     boton2 = tk.Button(ventana, text="Opción 2", font=("Arial", 14), width=20, command=accion) 
     boton2.pack(pady=10)

     boton3 = tk.Button(ventana, text="Opcion 3", font=("Arial",14),  whidth=20, command=accion)
     boton3.pack(pady=10)

     boton4 = tk.Button(ventana, text="Opcion 4", font=("Arial", 14), whidth=20, commamd=accion)
     boton4.pack(pady=10)

     def mostrar():
     limpiarVentana()
     label = tk.Label(ventana, text="Elegiste la Opción 1", font=("Arial", 16))
     label.pack(pady=20)
 
     boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
     boton_volver.pack(pady=10)
 
 def mostrarOpcion2():
     limpiarVentana()
     label = tk.Label(ventana, text="Elegiste la Opción 2", font=("Arial", 16))
     label.pack(pady=20)
 
     boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
     boton_volver.pack(pady=10)
