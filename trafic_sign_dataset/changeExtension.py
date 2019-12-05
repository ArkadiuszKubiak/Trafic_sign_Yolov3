import os
import sys
import re
from os.path import join
from os.path import splitext
from PIL import Image
from shutil import copyfile
def main():
    annotation_list_path = 'C:\\Users\\Arek\\Desktop\\YOLOv3-custom-training\\trafic_sign_dataset\\all_speed_limit.txt'
    annotation_files_path = 'C:\\Users\\Arek\\Desktop\\YOLOv3-custom-training\\trafic_sign_dataset\\annotations\\'
    new_annotation_files_path = 'C:\\Users\\Arek\\Desktop\\YOLOv3-custom-training\\trafic_sign_dataset\\spped_limit\\'
    work_dir = 'C:\\Users\\Arek\\Desktop\\YOLOv3-custom-training\\trafic_sign_dataset\\spped_limit\\' 
    with open(annotation_list_path) as f:
        lines = f.readlines()
    
    for filename in lines:
        matchObj = re.match( r'C:\\Users\\Arek\\Desktop\\YOLOv3-custom-training\\trafic_sign_dataset\\images\\((\d+)(\.[a-z]+ ))', filename, re.M|re.I)
        print(work_dir + str(matchObj[2])+".jpg")
        copyfile(annotation_files_path + str(matchObj[2]) + '.xml', new_annotation_files_path  + str(matchObj[2]) + '.xml')
if __name__ == '__main__':
    main()