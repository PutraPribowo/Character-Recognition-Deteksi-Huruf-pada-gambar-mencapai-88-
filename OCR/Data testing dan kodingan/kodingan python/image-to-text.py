import cv2
import pytesseract
import numpy as np
import argparse
import os
from PIL import Image
import sys

#untuk ekstrak path tesseract ocr
pytesseract.pytesseract.tesseract_cmd = r'D:\APLIKAS\ocr2\tesseract'

def get_string(img_path):
    # membaca gambar dan menjadi RGB
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)

    # merubah ke grayscale
    img_c = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
    # untuk mengurangi noise
    kernel = np.ones((1, 1), np.uint8)
    img_nd = cv2.dilate(img_c, kernel, iterations=1)
    img_ne = cv2.erode(img_nd, kernel, iterations=1)

    # menulis image sebelum merubahnya ke teks
    cv2.imwrite("thres.png", img_ne)

    # menggunakan tesseract
    result = pytesseract.image_to_string(Image.open("thres.png"))
    
    return result
     	
	
if __name__ == '__main__':
    from sys import argv

    if len(argv)<2:
        print("python image-to-text.py nama file")
    else:
        print('**********************')
        print('Nama: Putra Pribowo')
        print('Npm : 1617051005')
        print('**********************')
        print('--- Memulai ---')
		
        for i in range(1,len(argv)):
            print(argv[i])
            # memberikan informasi gambar ke teks
            print("\n")
            print('**********************')
            print("hasil string saja")
            print('**********************')
            print(get_string(argv[i]))
            print("\n")
            
            # memberikan informasi kotak estimasi
            print('**********************')
            print("gambar ke boxes")
            print('**********************')
            print(pytesseract.image_to_boxes(Image.open(argv[i])))
            print("\n")

            # memberikan informasi including boxes, confidences, baris and nomor baris
            print('**********************')
            print("gambar ke data")
            print('**********************')
            print(pytesseract.image_to_data(Image.open(argv[i])))
            print("\n")
            
            # memberikan informasi tentang orientasi dan skrip deteksi
            print('**********************')
            print("gambar ke osd")
            print('**********************')
            print(pytesseract.image_to_osd(Image.open(argv[i])))
            print()
            print()

        print('------ Sukses -------')
