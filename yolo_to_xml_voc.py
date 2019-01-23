import os
import xml.etree.cElementTree as ET
from PIL import Image

ANNOTATIONS_DIR_PREFIX = "annotations"

DESTINATION_DIR = "converted_labels"

CLASS_MAPPING = {
    '0': 'name'
    # Add your remaining classes here.
}


def create_root(file_prefix, width, height):
    root = ET.Element("annotations")
    root.set("verified","yes")
    ET.SubElement(root, "folder").text = "images"
    ET.SubElement(root, "filename").text = "{}.jpg".format(file_prefix)
    ET.SubElement(root,"path").text = "/home/arya/workspaip_01atm_slip.xml"

    source = ET.SubElement(root, "source")
    ET.SubElement(source, "database").text = "UNKNOWN"

    size = ET.SubElement(root, "size")
    ET.SubElement(size, "width").text = str(width)
    ET.SubElement(size, "height").text = str(height)
    ET.SubElement(size, "depth").text = "3"
    return root


def create_object_annotation(root, voc_labels):
    for voc_label in voc_labels:
        obj = ET.SubElement(root, "object")
        ET.SubElement(obj, "name").text = voc_label[0]
        ET.SubElement(obj, "pose").text = "Unspecified"
        ET.SubElement(obj, "truncated").text = str(0)
        ET.SubElement(obj, "difficult").text = str(0)
        bbox = ET.SubElement(obj, "bndbox")
        ET.SubElement(bbox, "xmin").text = str(voc_label[1])
        ET.SubElement(bbox, "ymin").text = str(voc_label[2])
        ET.SubElement(bbox, "xmax").text = str(voc_label[3])
        ET.SubElement(bbox, "ymax").text = str(voc_label[4])
    return root


def create_file(file_prefix, width, height, voc_labels):
    root = create_root(file_prefix, width, height)
    root = create_object_annotation(root, voc_labels)
    tree = ET.ElementTree(root)
    tree.write("{}/{}.xml".format(DESTINATION_DIR, file_prefix))


def read_file(file_path):
    file_prefix = file_path.split(".txt")[0]
    print ("file_prefix",file_prefix)
    image_file_name = "{}.jpeg".format(file_prefix)
    print ("image_file_name",image_file_name)
    print ("{}/{}".format("images", image_file_name))
    img = Image.open("{}/{}".format("images", image_file_name))
    w, h = img.size
    full_file_path = ANNOTATIONS_DIR_PREFIX + file_path
    with open(full_file_path, 'r') as file:
        lines = file.readlines()
        voc_labels = []
        for line in lines:
            voc = []
            line = line.strip()
            data = line.split()
            voc.append(CLASS_MAPPING.get(data[0]))
            bbox_width = float(data[3]) * w
            bbox_height = float(data[4]) * h
            center_x = float(data[1]) * w
            center_y = float(data[2]) * h
            voc.append(center_x - (bbox_width / 2))
            voc.append(center_y - (bbox_height / 2))
            voc.append(center_x + (bbox_width / 2))
            voc.append(center_y + (bbox_height / 2))
            voc_labels.append(voc)
        create_file(file_prefix, w, h, voc_labels)
    print("Processing complete for file: {}".format(file_path))


def start():
    if not os.path.exists(DESTINATION_DIR):
        os.makedirs(DESTINATION_DIR)
    for filename in os.listdir(ANNOTATIONS_DIR_PREFIX):
        if filename.endswith('txt'):
            print (filename)
            read_file(filename)
        else:
            print("Skipping file: {}".format(filename))


if __name__ == "__main__":

    DESTINATION_DIR = "save_xml_path"
    ANNOTATIONS_DIR_PREFIX = "text file path"
    start()
