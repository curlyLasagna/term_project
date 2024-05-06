import os
from random import randrange
import sqlite3
from sqlite3 import Error
import time
from flask import Flask
from flask_restful import Resource, Api
import numpy as np
import matplotlib.pyplot as plt
import cv2
import imutils
import easyocr

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

create_connection('/parking.db')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
    
    
    
def simulateEvent():
    imgDir = '/images'
    for filename in os.listdir(imgDir):
        img = cv2.imread(os.path.join(imgDir, filename))
        if img is not None:
            time.sleep(randrange(6))
            easyOcr(img)
    
    
simulateEvent()

def easyOcr (img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    bfilter = cv2.bilateralFilter(gray, 11, 11, 17)
    edged = cv2.Canny(bfilter, 30, 200)

    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    location = None

    for c in contours:
        approx = cv2.approxPolyDP(c, 10, True)
        if len(approx) == 4:
            location = approx
            break
        
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0, 255, -1)
    new_image = cv2.bitwise_and(img, img, mask = mask)

    (x, y) = np.where(mask == 255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    # Adding Buffer
    cropped_image = gray[x1:x2+3, y1:y2+3]
    
    reader = easyocr.Reader(['en'])
    result = reader.readtext(cropped_image)
    print(result)
    
