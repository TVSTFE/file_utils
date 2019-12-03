'''
some utils about xml files and image files
author:Chenlin Zhou
time:2019/12/3
'''

import xml.etree.ElementTree as ET
import os

class XmlUtils(object):

    def __init__(self):
        self.inputpath = '/home/zcl/PycharmProjects/SSD/datasets/VOC2007/Annotations'
        self.outpath = '/home/zcl/PycharmProjects/SSD-Tensorflow/datasets/data-ssd-voc/TRAIN'

    #modify parametor of xml file
    def XmlParaChange(self):
        listdir = os.listdir(self.inputpath)
        i = 0
        for file in listdir:
            if file.endswith('xml'):
                a, b = os.path.splitext(file)
                file = os.path.join(self.inputpath, file)
                tree = ET.parse(file)
                root = tree.getroot()
                i = i + 1
                #修改folder
                for object1 in root.findall('folder'):
                    object1.text='JPEGImages'
                    tree.write(file)
                    break
                #修改filename
                for object1 in root.findall('filename'):
                    object1.text= a
                    tree.write(file)
                    break
                
                #修改path
                for object1 in root.findall('path'):
                    #object1.text= file
                    object1.text = '/home/zcl/PycharmProjects/SSD/datasets/VOC2007/'
                    tree.write(file)
                    break

    #modify the file(bmp/jpg.etc) accordding to xml file
    def ModifyFileName(self):
        listdir = os.listdir(self.inputpath)
        i = 0
        for file in listdir:
            if file.endswith('xml'):
                a, b = os.path.splitext(file)
                file = os.path.join(self.inputpath, file)
                tree = ET.parse(file)
                root = tree.getroot()
                i = i + 1
                for object1 in root.findall('filename'):
                    # 修改对应的bmp文件名
                    file_bmp = os.path.join(os.path.abspath(self.inputpath), object1.text)  # 获取相应的bmp
                    file_bmp_rename = os.path.join(os.path.abspath(self.outpath), '0' + format(str(i), '0>5s') + '.bmp')
                    os.renames(file_bmp, file_bmp_rename)
                    # 修改xml文件名
                    file_xml = os.path.join(os.path.abspath(self.inputpath), str(a) + '.xml')
                    file_xml_rename = os.path.join(os.path.abspath(self.outpath), '0' + format(str(i), '0>5s') + '.xml')
                    os.renames(file_xml, file_xml_rename)
                    break

    #modify the name of jpg file
    def ModifyJpgFileName(self):
        listdir = os.listdir(self.inputpath)
        i = 0
        print(listdir)
        for file in listdir:
            print(file)
            if file.endswith('jpg'):
                a, b = os.path.splitext(file)
                print(a)
                i = i + 1
                file_jpg = os.path.join(os.path.abspath(self.inputpath), str(a) + '.jpg')
                file_jpg_rename = os.path.join(os.path.abspath(self.outpath), '0' + format(str(i), '0>5s') + '.jpg')
                os.renames(file_jpg, file_jpg_rename)

    #modify the name of xml file
    def ModifyXmlFileName(self):
        listdir = os.listdir(self.inputpath)
        i = 0
        for file in listdir:
            if file.endswith('xml'):
                a, b = os.path.splitext(file)
                i = i + 1
                file_xml = os.path.join(os.path.abspath(self.inputpath), str(a) + '.xml')
                file_xml_rename = os.path.join(os.path.abspath(self.outpath), '0' + format(str(i), '0>5s') + '.xml')
                os.renames(file_xml, file_xml_rename)



if __name__ == '__main__':
    XmlUtils().XmlParaChange()
