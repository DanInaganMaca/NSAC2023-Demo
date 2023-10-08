# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

#Workspace
outLoc = r"/home/carolina/Documentos/AppSpace/NSAC2023-Demo/pruebas_Carolina/nbandas"
inNetCDF = r"/home/carolina/Documentos/AppSpace/NSAC2023-Demo/pruebas_Carolina/images/EMIT_L2A_RFL_001_20230928T081247_2327105_035.nc"

#Variable
variable = "npp"
x_dimension = "lon"
y_dimension = "lat"
band_dimension = ""
dimension = "time"
valueSelectionMethod = "BY_VALUE"

nc_FP = arcpy.NetCDFFileProperties(inNetCDF)
nc_Dim = nc_FP.getDimensions()

for dimension in nc_Dim:
        if dimension == "time":
            top = nc_FP.getDimensionSize(dimension)
            for i in range(0, top):

                dimension_values = nc_FP.getDimensionValue(dimension, i)
                nowFile = str(dimension_values)
                nowFile = nowFile.translate(None, '/')
                # I needed only the years 2002
                if int(nowFile[-12]) > 6:

                    dv1 = ["time", dimension_values]
                    dimension_values = [dv1]

                    arcpy.MakeNetCDFRasterLayer_md(inNetCDF, variable, x_dimension, y_dimension, nowFile, band_dimension, dimension_values, valueSelectionMethod)
                    print "success"
                    outname = outLoc + nowFile

                   arcpy.CopyRaster_management(nowFile, outname, +".tif","", "", "", "NONE", "NONE", "")


                else: print "DATA OUT OF RANGE"‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍
