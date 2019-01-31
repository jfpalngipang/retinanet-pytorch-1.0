import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import csv

def generate_class_mapping():
    class_map_list = []
    fieldnames =  ['path_to_image','xmin','ymin','xmax','ymax','class']
    i = 0
    with open('./annotations.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=fieldnames)
        next(reader)
        for line, row in enumerate(reader):
            print(row['class'])
            value = (row['class'], i)
            i += 1
            class_map_list.append(value)
    column_name = ['class', 'id']
    df = pd.DataFrame(class_map_list, columns=column_name)
    return df


def main():
    df = generate_class_mapping()
    df.to_csv('class_mappings.csv', index=None)
    # image_path = os.path.join(os.getcwd(), 'Annotations')
    # xml_df = xml_to_csv(image_path)
    # xml_df.to_csv('annotations.csv', index=None)
    # print('Successfully converted xml to csv.')


main()