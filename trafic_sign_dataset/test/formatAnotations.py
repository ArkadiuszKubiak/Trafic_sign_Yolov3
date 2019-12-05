import os
import sys
import re
from os.path import join
from os.path import splitext
from PIL import Image
jpg_dir = 'C:\\Users\\Arek\\Desktop\\test\\' 
annot_dir = 'C:\\Users\\Arek\\Desktop\\test\\' 
def checkTheFile(fileName):
    file = open(annot_dir + fileName + ".xml", "r")
    data = file.readlines()
    print(jpg_dir + fileName + ".jpg ", end = '')
    for index in range(0, len(data)):
        if "<object>" in data[index]:
            matchObj = re.match( r'		<name>(\d+)</name>', data[index + 1], re.M|re.I)
            ClassName = matchObj.group(1)
            matchObj = re.match( r'			<xmin>(\d+)</xmin>', data[index + 6], re.M|re.I)
            xmin = matchObj.group(1)
            matchObj = re.match( r'			<ymin>(\d+)</ymin>', data[index + 7], re.M|re.I)
            ymin = matchObj.group(1)
            matchObj = re.match( r'			<xmax>(\d+)</xmax>', data[index + 8], re.M|re.I)
            xmax = matchObj.group(1)
            matchObj = re.match( r'			<ymax>(\d+)</ymax>', data[index + 9], re.M|re.I)
            ymax = matchObj.group(1)
            index = index + 12
            print(xmin + "," + ymin + "," + xmax + "," + ymax + "," + ClassName + " ", end = '')
    print(" ")    

for filename in os.listdir(jpg_dir):
    if ".jpg" == splitext(filename)[1]:
        checkTheFile(splitext(filename)[0])