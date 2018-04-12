import datetime
import os,sys
import csv

import csv
def write_headers_csv_for_input_file(OutputPath,output_dictionary,class_name):
    PATH = OutputPath + '/'+"input_data.csv"
    csvfile = open( PATH, 'aw')
    filename_9 = PATH
    fileEmpty = os.stat(filename_9).st_size == 0
    fieldnames = ['class','label', 'url', 'xmin','ymin','xmax','ymax','extra']
    print output_dictionary
    with csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if fileEmpty:
            writer.writeheader()
        writer.writerow(output_dictionary)

def rename(InputPath,OutputPath,filename,class_name):
    check_name = filename.split('.jpg')
    date_and_time = datetime.datetime.now()
    d_t = date_and_time.isoformat()
    d_t = str(d_t)
    d_t = d_t.replace(".", "")
    d_t = d_t.replace(":", "")
    d_t = d_t.replace("-", "")
    source_image_path = InputPath + filename
    # print source_image_path
    rename_image_path = OutputPath + class_name + '/'
    if not os.path.exists(rename_image_path):
        os.makedirs(rename_image_path)
    destination_image_name = rename_image_path + class_name + '_'+ d_t +'.jpg'
    only_image_name = class_name + '_'+ d_t +'.jpg'
    # print destination_image_name
    os.rename(source_image_path,destination_image_name)






