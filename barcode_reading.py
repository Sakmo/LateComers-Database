import cv2
from pyzbar import pyzbar
import time

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    global s
    for barcode in barcodes:
        barcode_info = barcode.data.decode('utf-8')
        identify(barcode_info)
        s+=1
    return frame

def identify(adm_no):
    #some function to return adm no. to user
    print(adm_no)

s = 0
camera = cv2.VideoCapture(1)  #0 for iriun, 1 for laptop camera
ret, frame = camera.read()    #2
while ret and s==0:
    ret, frame = camera.read()
    frame = read_barcodes(frame)
    cv2.imshow('Scan the ID card here', frame)
    if cv2.waitKey(1)==27:  #27 is the cv2 order of escape key
        break
camera.release()
cv2.destroyAllWindows()

'''
import cv2
from pyzbar import pyzbar

s = 0
def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        barcode_info = barcode.data.decode('utf-8')
        global s
        if s ==0:
            print(barcode_info)
            s+=1
    return frame
    
def main():    #1
    camera = cv2.VideoCapture(1)  #0 for iriun, 1 for laptop camera
    ret, frame = camera.read()    #2
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Scan the ID card here', frame)
        if cv2.waitKey(1)==27:  #27 is the cv2 order of escape key
            break
    camera.release()
    cv2.destroyAllWindows()
'''
