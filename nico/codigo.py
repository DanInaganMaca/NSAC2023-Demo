import netCDF4 as nc
import numpy as np
import open3d as o3d
import cv2
import rescaleFrame
import matplotlib.pyplot as plt

archivo_nc = './netCDF/EMIT_L2A_RFL_001_20230119T114235_2301907_004.nc'
dataset = nc.Dataset(archivo_nc, 'r')  # 'r' para lectura

variables = dataset.variables.keys()
print("Variables en el archivo:")
for variable in variables:
    print(variable)
variable = dataset.variables['reflectance']
datos = variable[:]
unidades = variable.units
descripcion = variable.long_name
print("VARIABLE: ", type(variable), variable.ndim, variable.shape)
print("DATOS: ", type(datos), datos[0].ndim, datos[0].shape)
print("UNIDADES: ", type(unidades), unidades)
print("DESCRIPCION: ", type(descripcion), descripcion)
print("pixel: ",  type(datos), datos[0][0].ndim, datos[0][0].shape)

imgs = list()

# Convierte la matriz MaskedArray a una matriz NumPy estándar
# Rellena las máscaras con 0
numpy_array = np.ma.filled(datos, fill_value=-999)
print("Numpy Array: ", type(numpy_array), numpy_array.shape, numpy_array.ndim)
# myIn = int(input("Ingrese la banda: " ))
# numpy_array[0] = image.ndim(0)
imgs = list()
imgs_color = list()
for band in range(0, 285, 5):
    # imgs.append(numpy_array[:, :,band])
    # print("Banda "+str(band),type(numpy_array[:, :,band]), numpy_array[:, :,band].ndim, numpy_array[:, :,band].shape)
    # if band == myIn:
    # imagen_array = numpy_array[:, :,band] * 255  # Simulamos una matriz de valores en el rango [0, 255]
    # imagen_array = np.clip(imagen_array, 0, 255).astype(np.uint8)
    imagen_opencv = cv2.cvtColor(
        numpy_array[:, :, band], cv2.COLOR_GRAY2BGR)  # Convertir a formato BGR
    imagen_gray = cv2.cvtColor(numpy_array[:, :, band], cv2.IMREAD_GRAYSCALE)
    imagen_gray = rescaleFrame.rescaleFrame(imagen_gray, 0.35)

    imgs.append(imagen_gray)
    imgs_color.append(imagen_opencv)

    # Guardar la imagen resultante
    # cv2.imwrite('fot\imagen_ajustada'+str(band)+'.jpg', imagen_gray)
    # imagen_gray = cv2.convertScaleAbs(imagen_gray)
    print("Banda: "+str(band), imagen_gray)
    # cmap = cv2.applyColorMap(imagen_opencv, cv2.COLORMAP_JET)  # Puedes elegir otro colormap en lugar de COLORMAP_JET

    # if band == 50:
    # imagen_color = cv2.merge(imgs_color[41:46])
    # print("imgColor:",type(imagen_color),imagen_color.shape)
    cv2.imshow('Imagen_'+str(band), imagen_gray)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    # imagen_gris_mapeada = (imagen_gray + 1) / 2.0

    # Calcular el histograma de la imagen mapeada

    histograma = cv2.calcHist([imagen_gray], [0], None, [256], [0, 1])

    # Mostrar el histograma
    plt.hist(imagen_gray.ravel(), 256, [0, 1])
    plt.xlabel('Valor de píxel')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Imagen en Gris (Valores mapeados a [0, 1])')
    plt.show()
