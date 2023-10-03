import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import rescaleFrame
import threading
'''

'''


def interfazGrafica():
    Hmin = 0
    Smin = 0
    Vmin = 0
    Hmax = None
    Smax = None
    Vmax = None
    # Función para actualizar los valores de los sliders

    def actualizar_sliders(event, returnValues=0):
        global Hmin, Smin, Vmin
        valor_slider1.set(slider1.get())
        valor_slider2.set(slider2.get())
        valor_slider3.set(slider3.get())
        valor_slider4.set(slider4.get())
        valor_slider5.set(slider5.get())
        valor_slider6.set(slider6.get())
        valor_slider7.set(slider7.get())
        Hmin = (slider1.get())
        Smin = (slider2.get())
        Vmin = (slider3.get())
        Hmax = (slider4.get())
        Smax = (slider5.get())
        Vmax = (slider6.get())
        sc = (slider7.get())
        # Convertir la imagen PIL a un formato compatible con Tkinter
        # imagen_tk = ImageTk.PhotoImage(imagen_pil)

        # Crear un widget Label para mostrar la imagen
        # etiqueta_imagen = ttk.Label(ventana, image=imagen_tk)
        # etiqueta_imagen.place(x=350, y=75)
        # etiqueta_imagen.pack()

        # Mostrar la imagen en la ventana
        # etiqueta_imagen.image = imagen_tk  # Esto es importante para evitar que la imagen se elimine de la memoria

        print("Hmin: ", Hmin, "Smin: ", Smin, "Vmin: ", Vmin,
              "Hmax: ", Hmax, "Smax: ", Smax, "Vmax: ", Vmax)
        # Escribir en un archivo
        with open('datos.txt', 'w') as archivo:
            archivo.write(str(Hmin)+","+str(Smin)+","+str(Vmin) +
                          ","+str(Hmax)+","+str(Smax)+","+str(Vmax)+","+str(sc))

    # Función para mostrar los valores de los sliders
    def mostrar_valores():
        texto = f"H:{valor_slider1.get()},S:{valor_slider2.get()},V: {valor_slider3.get()}"
        etiqueta_resultado.config(text=texto)

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Color-contour Segmentation- HSV Space")
    ventana.geometry("320x400")  # Ancho x Alto en píxeles
    # imagen = cv2.imread('sattco.jpg')  # Reemplaza 'tu_imagen.jpg' con la ruta de tu imagen
    # imagen = rescaleFrame.rescaleFrame(imagen,scale=0.5)
    # cv2.imshow('Imagen Original', imagen)
    # cv2.waitKey(0)
    # =======================================
    # Cargar la imagen con PIL
    # imagen_pil = Image.fromarray(imagen)  # Reemplaza "imagen.jpg" con la ruta de tu imagen
    # **********************************************************************************************
    # Slider 1 HUE (COLOR) 0-179 FOR OPENCV
    etiqueta_slider1 = ttk.Label(ventana, text="H min")
    etiqueta_slider1.place(x=20, y=25)
    # etiqueta_slider1.pack()
    slider1 = ttk.Scale(ventana, from_=0, to=179, orient="horizontal")
    # Puedes ajustar las coordenadas (x, y) según tu preferencia
    slider1.place(x=20, y=50)
    # slider1.pack()
    valor_slider1 = tk.DoubleVar()
    campo_texto1 = ttk.Entry(ventana, textvariable=valor_slider1)
    campo_texto1.place(x=20, y=75)
    # campo_texto1.pack()
    # **********************************************************************************************
    # Slider 2 SATURATION  0-255 FOR OPENCV  SINCE BLANK TO THE MAX COLOR
    etiqueta_slider2 = ttk.Label(ventana, text="S min")
    etiqueta_slider2.place(x=20, y=125)
    # etiqueta_slider2.pack()
    slider2 = ttk.Scale(ventana, from_=0, to=255, orient="horizontal")
    slider2.place(x=20, y=150)
    # slider2.pack()
    valor_slider2 = tk.DoubleVar()
    campo_texto2 = ttk.Entry(ventana, textvariable=valor_slider2)
    campo_texto2.place(x=20, y=175)
    # campo_texto2.pack()
    # **********************************************************************************************
    # Slider 3 VALUE  0-255 FOR OPENCV  SINCE DARK TO THE MAX brightness
    etiqueta_slider3 = ttk.Label(ventana, text="V min")
    etiqueta_slider3.place(x=20, y=225)
    # etiqueta_slider3.pack()
    slider3 = ttk.Scale(ventana, from_=0, to=255, orient="horizontal")
    slider3.place(x=20, y=250)
    # slider3.pack()
    valor_slider3 = tk.DoubleVar()
    campo_texto3 = ttk.Entry(ventana, textvariable=valor_slider3)
    campo_texto3.place(x=20, y=275)
    # campo_texto3.pack()
    # ************************************************************************************************
    # Slider 4 HUE (COLOR) 0-179 FOR OPENCV
    etiqueta_slider4 = ttk.Label(ventana, text="H max")
    etiqueta_slider4.place(x=175, y=25)
    # etiqueta_slider1.pack()
    slider4 = ttk.Scale(ventana, from_=0, to=179, orient="horizontal")
    # Puedes ajustar las coordenadas (x, y) según tu preferencia
    slider4.place(x=175, y=50)
    # slider1.pack()
    valor_slider4 = tk.DoubleVar()
    campo_texto4 = ttk.Entry(ventana, textvariable=valor_slider4)
    campo_texto4.place(x=175, y=75)
    # campo_texto1.pack()
    # **********************************************************************************************
    # Slider 2 SATURATION  0-255 FOR OPENCV  SINCE BLANK TO THE MAX COLOR
    etiqueta_slider5 = ttk.Label(ventana, text="S max")
    etiqueta_slider5.place(x=175, y=125)
    # etiqueta_slider2.pack()
    slider5 = ttk.Scale(ventana, from_=0, to=255, orient="horizontal")
    slider5.place(x=175, y=150)
    # slider2.pack()
    valor_slider5 = tk.DoubleVar()
    campo_texto5 = ttk.Entry(ventana, textvariable=valor_slider5)
    campo_texto5.place(x=175, y=175)
    # campo_texto2.pack()
    # **********************************************************************************************
    # Slider 3 VALUE  0-255 FOR OPENCV  SINCE DARK TO THE MAX brightness
    etiqueta_slider6 = ttk.Label(ventana, text="V max")
    etiqueta_slider6.place(x=175, y=225)
    # etiqueta_slider3.pack()
    slider6 = ttk.Scale(ventana, from_=0, to=255, orient="horizontal")
    slider6.place(x=175, y=250)
    # slider3.pack()
    valor_slider6 = tk.DoubleVar()
    campo_texto6 = ttk.Entry(ventana, textvariable=valor_slider6)
    campo_texto6.place(x=175, y=275)
   # ================================================================
    # Slider 3 VALUE  0-255 FOR OPENCV  SINCE DARK TO THE MAX brightness
    etiqueta_slider7 = ttk.Label(ventana, text="Scale Value")
    etiqueta_slider7.place(x=200, y=350)
    # etiqueta_slider3.pack()
    slider7 = ttk.Scale(ventana, from_=1, to=2, orient="horizontal")
    slider7.place(x=200, y=300)
    # slider3.pack()
    valor_slider7 = tk.DoubleVar()
    campo_texto7 = ttk.Entry(ventana, textvariable=valor_slider7)
    campo_texto7.place(x=200, y=325)
    # Configurar la llamada a la función actualizar_sliders cuando los sliders se muevan
    slider1.bind("<Motion>", actualizar_sliders)
    slider2.bind("<Motion>", actualizar_sliders)
    slider3.bind("<Motion>", actualizar_sliders)
    slider4.bind("<Motion>", actualizar_sliders)
    slider5.bind("<Motion>", actualizar_sliders)
    slider6.bind("<Motion>", actualizar_sliders)
    slider7.bind("<Motion>", actualizar_sliders)
    # Botón para mostrar valores
    boton = ttk.Button(ventana, text="Mostrar Valores",
                       command=mostrar_valores)
    # boton.pack()
    boton.place(x=100, y=320)
    etiqueta_resultado = ttk.Label(ventana, text="")
    etiqueta_resultado.place(x=20, y=350)
    # etiqueta_resultado.pack()
    ventana.mainloop()

    # Iniciar el bucle principal de la GUI
