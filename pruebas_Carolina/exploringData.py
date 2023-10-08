import xarray as xr
import hvplot.xarray
import numpy as np
import matplotlib

#matplotlib.use('TKAgaa')
#hvplot.extension('matplotlib')

def openFile():
	
	try:
		#print('.................')
		file_nc = '/home/carolina/Documentos/AppSpace/NSAC2023-Demo/pruebas_Carolina/images/EMIT_L2A_RFL_001_20230928T081247_2327105_035.nc'
		#file =   xr.open_dataset(filename_or_obj = file_nc) 
		fileN =   xr.open_dataset(filename_or_obj = file_nc) 
		print(fileN.spatial_ref)
		
		dimensions = dict(fileN.dims)
		variables = fileN .variables
		attributes = fileN .attrs
		k = dimensions.keys()
		#ds_nc = xr.groups.keys()
		print(k)
		# #print(file)
		w_b = xr.open_dataset(file_nc, group = 'sensor_band_parameters')
		print(w_b)
		loc = xr.open_dataset(file_nc,group='location')
		print(loc)
		ds = fileN.assign_coords({'downtrack':(['downtrack'], fileN.downtrack.data), 'crosstrack':(['crosstrack'], fileN.crosstrack.data)})
		print(ds)
		###
		dsF = ds.swap_dims({'bands':'wavelengths'})
		#visualizing spectra - non orthorectified
		print(dsF)
		example = dsF['reflectance'].sel(downtrack=660, crosstrack=370)
		fg =example.hvplot.line(y='reflectance', x = 'wavelengths', color = 'black')
		hvplot.show(fg)
		#dsF['reflectance'].data[:,:,dsF['good_wavelengths'].data==0] = np.nan
		print('..........................3')
		
		##fg1 = dsF['reflectance'].sel(downtrack=660,crosstrack=370).hvplot.line(y='reflectance',x='wavelengths', color='black')
		print('..........................4')
		#show()
		print('..........................5')
		#refl850 = dsF.sel(wavelengths=850, method='nearest')
		#fgp = refl850.hvplot.image(cmap='viridis', aspect = 'equal', rasterize=True) 
		#hvplot.show(fgp)
		

		

	except Exception as err:
		print('Exception', err)
        

openFile()   
    
