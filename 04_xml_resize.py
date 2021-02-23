from os import walk
import xml.etree.ElementTree as ET

mypath = "C:/Users/thirat/Documents/git/labelImg/dataset/HR/"
# checked = ["IMG_20201208_113851.xml", "IMG_20201208_113858.xml","IMG_20201208_113904.xml"]
checked = []

for (_, _, filenames) in walk(mypath):
    for file in filenames:
        if (".xml" in file) and (file not in checked):
            mytree = ET.parse(mypath + file)
            myroot = mytree.getroot()


            # iterating throught the price values.
            for p11 in myroot.iter('width'):
                # updates the price value
                p11.text = str(1280)
            # iterating throught the price values.
            for p12 in myroot.iter('height'):
                # updates the price value
                p12.text = str(1280)
            # iterating throught the price values.
            for p1 in myroot.iter('xmin'):
                # updates the price value
                p1.text = str(int(p1.text) /2)
            for p2 in myroot.iter('xmax'):
                # updates the price value
                p2.text = str(int(p2.text) /2)
            for p3 in myroot.iter('ymin'):
                # updates the price value
                p3.text = str(int(p3.text) /2)
            for p4 in myroot.iter('ymax'):
                # updates the price value
                p4.text = str(int(p4.text) /2)
            mytree.write(mypath + file)