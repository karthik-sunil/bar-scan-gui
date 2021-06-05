#!/usr/bin/env python
# coding: utf-8

# In[13]:


import tkinter as tk
from pyzbar import pyzbar
import cv2

#frame = tk.Tk()
#frame.title("TextBox Input")
#frame.geometry('400x200')


def ImageScan():
    img = inputtxt.get(1.0, "end-1c")
    path = r"C:\Users\Anu\Desktop\BB\Barcode-Reader-master\Barcode-Reader-master\BarcodeDatasets\DATASET"
    img = path+'\\'+img
    lbl.config(text = "Image file provided: "+img)
    barcode_data = bar_scanner(img)
    #barcode_data = 'it is scanned'
    if barcode_data:
        lab = tk.Label(frame,text = 'Decoded')
        lab.pack()
        outputtxt = tk.Text(frame,height = 2, width = 45)
        outputtxt.pack()
        outputtxt.insert(tk.END, barcode_data)
        
def bar_scanner(img):
    print(img)
    barcode_data=[]
    image = cv2.imread(img)
    #cv2.imshow(image)
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        barcodeData = barcode.data.decode('utf-8')
        barcodeType = barcode.type
        text = "{} ( {} )".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)

        barcode_data.append("Found Type : {} Barcode : {}".format(barcodeType, barcodeData))
    cv2.waitKey(0)
    return(barcode_data)

def input_clear():
    inputtxt.delete('1.0',tk.END)
    #outputtxt.delete('1.0',tk.END)

    


frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
    
inputtxt = tk.Text(frame,height = 2,width = 20)
inputtxt.pack()

scanButton = tk.Button(frame, text = "Scan Code", command = ImageScan)
scanButton.pack()

clearButton = tk.Button(frame, text = "Clear", command = input_clear)
clearButton.pack()

lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()


# In[ ]:




