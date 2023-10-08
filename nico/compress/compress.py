import netCDF4 as nc
from netCDF4 import Dataset

# Abre el archivo NetCDF en modo lectura
archivo_entrada = r'../netCDF/EMIT_L2A_RFLUNCERT_001_20230119T114235_2301907_004.nc'

# Crea un nuevo archivo NetCDF comprimido en modo escritura
archivo_salida = nc.Dataset(
    './archivo_salida.nc', 'w', format='NETCDF4', zlib=True)

data_archivo_entrada = Dataset(archivo_entrada)

print(data_archivo_entrada)

print("variables:")
print(data_archivo_entrada.variables.keys())

# Copia las variables del archivo de entrada al archivo de salida
for nombre_variable, variable in archivo_entrada.variables.items():
    # Crea una variable con el mismo nombre y tipo en el archivo de salida
    variable_salida = archivo_salida.createVariable(
        nombre_variable, variable.datatype, variable.dimensions)

    # Copia los atributos de la variable
    variable_salida.setncatts({k: variable.getncattr(k)
                              for k in variable.ncattrs()})

    # Copia los datos de la variable
    variable_salida[:] = variable[:]

# Cierra los archivos
archivo_entrada.close()
archivo_salida.close()
