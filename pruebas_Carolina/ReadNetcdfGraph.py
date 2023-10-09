import xarray as xr
import hvplot.xarray
import netCDF4 as nc
import numpy as np
import cv2 
import matplotlib.pyplot as plt
import rescaleFrame
import time
import pandas as pd



def openFile():
	
	try:    
      # file_nc = 'E:/SpaceApp/Images/EMIT_L2A_RFL_001_20230928T081247_2327105_035.nc'
		file_nc = 'E:/SpaceApp/Images/EMIT_L2A_RFL_001_20230119T114235_2301907_004.nc'
		fileN =   xr.open_dataset(filename_or_obj = file_nc) 
	
		dimensions = dict(fileN.dims)
		variables = fileN .variables
		attributes = fileN .attrs
		k = dimensions.keys()

		w_b = xr.open_dataset(file_nc, group = 'sensor_band_parameters')

		loc = xr.open_dataset(file_nc,group='location')

		ds = fileN.assign_coords({'downtrack':(['downtrack'], fileN.downtrack.data), 'crosstrack':(['crosstrack'], fileN.crosstrack.data)})
                
		return ds

	except Exception as err:
		print('Exception', err)
        
def graph(x, y, ds):
    #label =  1 #agua
    #label = 2 #urbanizacion
    #label = 3 # vegetacion
    label = 4 # suelo 
    dsF = ds.swap_dims({'bands':'wavelengths'})
    
    dsF['reflectance'].data[dsF['reflectance'].data<0] = np.nan
   
    example = dsF['reflectance'].sel(downtrack=x, crosstrack= y)
      #example = dsF['reflectance'].sel(downtrack=lon, crosstrack=lat)
    fg =example.hvplot.line(y='reflectance', x = 'wavelengths', color = 'black')
    # hvplot.show(fg)
    
    # fg =example.hvplot.line(y='reflectance', x = 'wavelengths', color = 'black')
	 #print("FG : ", fg," Type: ", type(fg))
     
    reflect = fg['reflectance']
    print(type(reflect))
   
    wavelen = fg['wavelengths']
       
    archivoH = "E:/SpaceApp/datosH.csv"
    df = pd.DataFrame(wavelen).T
    df['Label'] = 'Etiqueta' 

    df1 = pd.DataFrame(reflect).T
    df1['Etiqueta'] = label

    df1.to_csv(archivoD, index=None, mode='a', sep=',', header = False, na_rep=np.nan)
    archivoD

    
    df.to_csv(archivoH, index=None, mode='a', sep=',', na_rep=np.nan, header = False )
    data = {'wavelengths': wavelen, 'reflectance': reflect}

    time.sleep(1)

    df = pd.DataFrame(data)
    plt.plot(df['wavelengths'], df['reflectance'])
    plt.xlabel('Longitud de onda')
    plt.ylabel('Reflectancia')
    plt.title('Gráfico de Reflectancia')
    plt.show()
    
    
    
      
def click_event(event, x,y, flags, params):
    global coordenadas
    
    if( event == cv2.EVENT_LBUTTONDOWN):
        print(x, ' ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(img,str(x) + ',' +
                    str(y), (x,y), font, 
                    1, (255, 0, 0), 2 )
        graph(x, y, file)
        cv2.imshow('imagen', img) 
    if event==cv2.EVENT_RBUTTONDOWN: 
  
        print(x, ' ', y) 
  
        # displaying the coordinates 
        # on the image window 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        b = img[y, x, 0] 
        g = img[y, x, 1] 
        r = img[y, x, 2] 
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r), 
                    (x,y), font, 1, 
                    (255, 255, 0), 2) 
        graph(x, y, file)
        cv2.imshow('imagen', img) 
        
def image():
    global archivoD
    archivoD = "E:/SpaceApp/datos.csv"
    
    
    C = 'E:/SpaceApp/Images/outcomes'
    archivo_nc = 'E:/SpaceApp/Images/EMIT_L2A_RFL_001_20230119T114235_2301907_004.nc'

    dataset = nc.Dataset(archivo_nc, 'r')  # 'r' para lectura

    variables = dataset.variables.keys()
    print("Variables en el archivo:")
    for variable in variables:
        print(variable)
    variable = dataset.variables['reflectance']
    datos = variable[:]
    unidades = variable.units
    descripcion = variable.long_name

    # Convierte la matriz MaskedArray a una matriz NumPy estándar
    numpy_array = np.ma.filled(datos, fill_value=np.nan)  # Rellena las máscaras con 0
    print("Numpy Array: ",type(numpy_array), numpy_array.shape, numpy_array.ndim)

    imagen_gray = cv2.cvtColor(numpy_array[:, :,10], cv2.IMREAD_GRAYSCALE)
    
    
    return imagen_gray

       
if __name__=="__main__": 
    file = openFile()
    global coordenadas

    img = image() 
    img = rescaleFrame.rescaleFrame(img,1)
    cv2.imshow('imagen', img)
    cv2.setMouseCallback('imagen', click_event)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows() 


    