import cv2 as cv
def rescaleFrame(frame,scale=1):
    width = int(frame.shape[1] * scale) #ancho
    height = int(frame.shape[0] * scale) #alto
    dimensions = (width,height)          #tupla que contiene las dimensiones reales
    print("Dimensions: ",width ,"x", height,frame.shape[1],"  Type:", type(dimensions))
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
