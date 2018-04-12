import os
import cv2
import numpy as np
import csv_file
import annotation
class_name = "intern_2"
label = "2"
mac = 111
InputPath = "/Users/pallawi/dev/attendance/Data/frames/" + class_name + "/"
OutputPath = "/Users/pallawi/dev/attendance/Data/frames/" + class_name + "/"
garbage_path = "/Users/pallawi/dev/attendance/Data/frames/Dustbin/"



def rename_all(InputPath,OutputPath,class_name):
    for filename in os.listdir(InputPath):
        csv_file.rename(InputPath,OutputPath,filename,class_name)

def manager_styfi_attendance(OutputPath,class_name,label,garbage_path):
    image_folder_path = OutputPath
    for filename in os.listdir(image_folder_path):
        # print " Running",image_folder_path
        face_locations,image_copy,image_path = annotation.automatic_annotation(image_folder_path,filename,class_name)
        print "face_locations",face_locations
        pink = face_locations
        destination = garbage_path + filename
        if (pink == []):
            os.rename(image_path,destination)
            continue
        else:
            top = face_locations[0][0]
            right= face_locations[0][1]
            bottom = face_locations[0][2]
            left = face_locations[0][3]

            output_dictionary = {}
            # left = left.split('L')
            # top = top.split('L')
            # right = right.split('L')
            # bottom= bottom.split('L')
            output_dictionary["xmin"]= left
            output_dictionary["ymin"]= top
            output_dictionary["xmax"]= right
            output_dictionary["ymax"]= bottom
            print "------annotated----",filename
            output_dictionary["url"]= filename
            output_dictionary["class"] = class_name
            output_dictionary["label"] = label
            # ['class','label', 'url', 'xmin','ymin','xmax','ymax','extra']
            csv_file.write_headers_csv_for_input_file(OutputPath,output_dictionary,class_name)
            label_image = cv2.rectangle(image_copy,(output_dictionary["xmin"],output_dictionary["ymin"]),(output_dictionary["xmax"],output_dictionary["ymax"]),(0,255,0),3)
            # cv2.imshow("check image",label_image)
            # cv2.waitKey(5)



if __name__ == '__main__':
    # if (mac == 000):
        # rename_all(InputPath,OutputPath,class_name)
    if (mac == 111):
        manager_styfi_attendance(OutputPath,class_name,label,garbage_path)
