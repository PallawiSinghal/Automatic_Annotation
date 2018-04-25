import os
import cv2
import numpy as np
import face_recognition #This is from dlib library which gives the face location.

def automatic_annotation(image_folder_path,filename,class_name):
    image_path = image_folder_path + '/' + filename

    print "--input for annotation--",filename
    image = cv2.imread(image_path,1)
    length = len(image)
    print "length",length
    if (length  > 0 ):
        image_copy = image.copy()
        face_locations = face_recognition.face_locations(image)
    else:
        print "-----------------------------Better luck next time --------------------------------"
    return face_locations,image_copy,image_path
