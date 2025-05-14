from tkinter import*
import tkinter as tk

def descargarPortada():
    urlImagen = "https://github.com/rodripiersi/Imagenes/blob/main/Portada.png?raw=true"
    datosImagen = urlopen(urlImagen)  # Descargar la imagen
    imagenBinaria = datosImagen.read()  # Obtener los datos de la imagen
    # Paso 2: Convertir los datos binarios en una imagen que podamos mostrar
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

def descargarSantiago():
    urlImagen = "https://github.com/rodripiersi/Imagenes/blob/main/Portada.png?raw=true"
    datosImagen = urlopen(urlImagen)  # Descargar la imagen
    imagenBinaria = datosImagen.read()  # Obtener los datos de la imagen
    # Paso 2: Convertir los datos binarios en una imagen que podamos mostrar
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen
def descargarKirby():
    urlImagen = "https://github.com/rodripiersi/Imagenes/blob/main/Portada.png?raw=true"
    datosImagen = urlopen(urlImagen)  # Descargar la imagen
    imagenBinaria = datosImagen.read()  # Obtener los datos de la imagen
    # Paso 2: Convertir los datos binarios en una imagen que podamos mostrar
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen
def descargarBarbieri():
    urlImagen = "https://github.com/rodripiersi/Imagenes/blob/main/Portada.png?raw=true"
    datosImagen = urlopen(urlImagen)  # Descargar la imagen
    imagenBinaria = datosImagen.read()  # Obtener los datos de la imagen
    # Paso 2: Convertir los datos binarios en una imagen que podamos mostrar
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen
def descargarFondo():
    urlImagen = "https://github.com/rodripiersi/Imagenes/blob/main/Portada.png?raw=true"
    datosImagen = urlopen(urlImagen)  # Descargar la imagen
    imagenBinaria = datosImagen.read()  # Obtener los datos de la imagen
    # Paso 2: Convertir los datos binarios en una imagen que podamos mostrar
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

def opciones():
    Label(ventana,text="funciones",font=("arial",16)).place(x=500,y=100)
    Button(ventana,text="integrantes",font=("Arial",12), bg="#A9A9A9").place(x=500,y=200)
    Button(ventana,text="chicas",font=("Arial",12), bg="#A9A9A9").place(x=500,y=300)
    Button(ventana,text="chicos",font=("Arial",12), bg="#A9A9A9").place(x=500,y=400)



def limpiar_ventana():
    #recorremos todos los widgets (elementos gráficos) que están dentro
    for widget in ventana.winfo_children():
        #Eliminamos cada widget para limpiar la ventana completamente
        widget.destroy()

def main():
    global ventana
    global alto
    global ancho
    
    ventana=tk.Tk()
    ventana.configure(bg="#900c3f")
    ventana.title("Promo Informàtica 2025")
    
    ancho = ventana.winfo_screenwidth()  # Obtengo el ancho del escritorio
    alto = ventana.winfo_screenheight()  # Obtengo el alto del escritorio
    ventana.geometry(f"{ancho}x{alto}")
    
    opciones()

    ventana.mainloop()

if __name__=="__main__":
    main()
    
