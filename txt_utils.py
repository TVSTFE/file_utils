'''
some utils about xml files and image files
author:Chenlin Zhou
time:2019/12/3
'''
import cv2
import shutil
import os
import xml.etree.ElementTree as ET
import numpy as np

class Txt_Utils(object):

    def _init_(self):

        #txt for reading or writting
        self.imput_path = '/home/zcl/独立代码/train.txt'

        #copy files
        self.new_path = ''
        self.old_path = ''

        #xml to txt /voc to yolo
        self.xml_path = ''
        self.image_path = ''
        self.txt_path = ''

    #parse_annotaton for txt line
    def parse_annotation(self, annotation):
        line = annotation.split()
        image_path = line[0]
        if not os.path.exists(image_path):
            raise KeyError("%s does not exist ... " % image_path)
        image = np.array(cv2.imread(image_path))
        bboxes = np.array([list(map(int, box.split(','))) for box in line[1:]])
        '''
        bboxes = np.array([list(map(int, box.split(','))) for box in line[1:]]) 等效以下代码:
        bboxes_temp = []
        for box in line[1:]:
            bboxes_temp.append(list(map(int,box.split(',') )))
        bboxes = np.array(bboxes_temp)
        '''
        return image_path, bboxes

    # txt read
    def txt_read(self):
        annotations = []
        with open(self.imput_path, 'r') as f:
            txt = f.readlines()
            annotations = [line.strip() for line in txt if len(line.strip().split()[1:]) != 0]
        f.close()
        return annotations


    #txt write
    def txt_write(self):
        trainval_path = open(os.path.join(self.imput_path ,'trainval.txt'),'w+')
        for trainval_xml in self.new_path:
            trainval_path.write(trainval_xml+'\n')
        trainval_path.close()


    #txt writting according to xml annotation
    def xml_to_txt(self):
        writeList = []
        for xml_name in os.listdir(self.xml_path):
            #ground_truth of the object
            xmin = []
            ymin = []
            xmax = []
            ymax = []

            tree = ET.parse(self.xml_path + '/' + xml_name)
            root = tree.getroot()

            #gain absolute path for image
            for path in root.iter('path'):
                xml_path_img = path.text
                path_img = self.image_path + xml_path_img[-10:-4] + '.bmp'
                writeList.append(path_img + ' ')


            #gain name and ground_truth of object
            for ob in root.iter('object'):
                name = []
                for i in ob.iter('name'):
                    name.append(i.text)
                for bndbox in ob.iter('bndbox'):
                    for i in bndbox.iter('xmin'):
                        xmin.append(i.text)
                    for i in bndbox.iter('ymin'):
                        ymin.append(i.text)
                    for i in bndbox.iter('xmax'):
                        xmax.append(i.text)
                    for i in bndbox.iter('ymax'):
                        ymax.append(i.text)
            for i in range(0, len(xmin)):
                writeList.append(xmin[i] + ',')
                writeList.append(ymin[i] + ',')
                writeList.append(xmax[i] + ',')
                writeList.append(ymax[i] + ',')

                if i == len(xmin) - 1:
                    writeList.append('0')
                elif i < len(xmin) - 1:
                    writeList.append('0' + ' ')
            writeList.append('\n')

        #write into path_txt according to writeList
        file = open(self.txt_path, 'w')
        for annotation  in writeList:
            file.write(str(annotation))
        file.close()

    #copy files
    def copy_file(self):
        file_name = 0
        old_file = os.path.join(os.path.abspath(self.old_path), str(file_name) + '.txt')
        new_file = os.path.join(os.path.abspath(self.new_path), str(file_name) + '.txt')
        shutil.copyfile(old_file, new_file)  # 复制
        # shutil.move(old_file, new_file)  # 移动

if __name__ == '__main__':
    Txt_Utils().copy_file()



