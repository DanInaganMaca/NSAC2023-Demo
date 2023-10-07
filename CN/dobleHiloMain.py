import threading
import interfazGrafica
import cv2
import numpy as np
import rescaleFrame 
# Función para actualizar la imagen según los valores de umbral
cnt_Count = 0
def actualizar_imagen(HminIn,SminIn,VminIn,HmaxIn,SmaxIn,VmaxIn):
    # Crea una máscara usando los valores de umbral en HSV
    lower_color = np.array([HminIn, SminIn, VminIn])
    upper_color = np.array([HmaxIn, SmaxIn, VmaxIn])
    mask = cv2.inRange(hsv_image, lower_color, upper_color)
    
    # Aplica la máscara a la imagen original
    resultado = cv2.bitwise_and(original_image, original_image, mask=mask)
    #resultado = cv2.Canny(resultado,50,255)
    # Aplica el filtro de mediana con un tamaño de kernel (ventana) específico
    #resultado = cv2.medianBlur(resultado, 5)  # El segundo argumento es el tamaño del kernel (ventana)
    # Convierte la imagen HSV a RGB
    im_rgb = cv2.cvtColor(resultado, cv2.COLOR_HSV2RGB)
    # Define el kernel (elemento estructurante) para la erosión y la dilatación
    kernelSz = np.ones((3, 3), np.uint8)
    # Realiza la erosión
    im_erd = cv2.erode(im_rgb, kernelSz, iterations=3)
    # Realiza la dilatación en la imagen erosionada
    im_dlt = cv2.dilate(im_erd, kernelSz, iterations=3)
    im_dlt = cv2.medianBlur(im_dlt, 3)  # El segundo argumento es el tamaño del kernel (ventana)

    # Convierte la imagen RGB a escala de grises
    im_gr = cv2.cvtColor(im_dlt, cv2.COLOR_RGB2GRAY)
    # Encuentra los contornos en la imagen
    countr, hrchy = cv2.findContours(im_gr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    #countr2, hrchy2 = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

    #print(f"Contourns: {countr}):")
    cv2.drawContours(resultado, countr, -1, (0, 255, 0), 1)
    #cv2.drawContours(mask, countr, -1, (0, 255, 0), 2)

    countCnt = 0
    for count in countr:
        x, y, w, h = cv2.boundingRect(count)  # Obtiene las coordenadas y dimensiones del rectángulo del contorno
        cv2.rectangle(resultado, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Dibuja el rectángulo rojo
        #cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 255, 255), 2)  # Dibuja el rectángulo rojo

        # Muestra el número de objeto en el rectángulo
        countCnt += 1
        cv2.putText(resultado, str(countCnt), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        #cv2.putText(mask, str(countCnt), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)




    # Muestra la imagen resultante
    #cv2.namedWindow('Imagen Tierra')
    cv2.imshow('Im Cartogr', resultado)
    cv2.imshow('Im Mask', mask)

# Lee la imagen original
original_image = cv2.imread('sattco.jpg')
original_image = rescaleFrame.rescaleFrame(original_image,1)
#original_image = cv2.Canny(original_image,70,255)
# Convierte la imagen a espacio de color HSV

# Dividir la imagen en canales RGB
b, g, r = cv2.split(original_image)

# Mostrar los canales en una sola figura
channels = np.hstack((b, g, r))
#cv2.imshow('BGR', channels)
# Calcular la "blueness"
blueness = cv2.subtract(b, np.maximum(r, g))
#cv2.imshow('Blue', blueness)

# Aplicar umbral para segmentar el primer plano
ret, mask2 = cv2.threshold(blueness, 45, 255, cv2.THRESH_BINARY_INV)

hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

# Crear hilos para mostrar las ventanas
hilo_tkinter = threading.Thread(target=interfazGrafica.interfazGrafica)
#hilo_opencv = threading.Thread(target=ejSatelite.ejSatelite)
# Iniciar los hilos
#hilo_opencv.start()
hilo_tkinter.start()
while True:

    with open('datos.txt', 'r') as archivo:
        valor = str(archivo.read())
        if valor != '':
            #Separar los valores con comas (,) y convertirlos a flotantes
            valor = valor.split(",")
            Hmin,Smin,Vmin,  Hmax,Smax,Vmax,sc = float(valor[0]),float(valor[1]),float(valor[2]),float(valor[3]),float(valor[4]),float(valor[5]),float(valor[6])-1
        else:
            #Si esta vacio el Txt se deja como flotante = 0, sino genera error
            valor = float(0)

    #Leer valores de Txt como lectura
    print(f'Values: Hmin:{Hmin}, Smin:{Smin} Vmin:{Vmin} Hmax:{Hmax}, Smax:{Smax} Vmax:{Vmax} Scale:{sc} ')
    actualizar_imagen(Hmin,Smin,Vmin,Hmax,Smax,Vmax)

    # Captura eventos de teclado
    #key = cv2.waitKey(1) & 0xFF
    
    # Si se presiona la tecla 'q', salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cierra la ventana de visualización y libera los recursos
cv2.destroyAllWindows()

#print(type(hilo_opencv), hilo_opencv)
#print(hilo_opencv.is_alive())

   