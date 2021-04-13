from os import walk
import xml.etree.ElementTree as ET

mypath = "C:/Users/thirat/Documents/git/labelImg/dataset/HR/"
# checked = ["IMG_20201208_113851.xml", "IMG_20201208_113858.xml","IMG_20201208_113904.xml"]

for (_, _, filenames) in walk(mypath):
    for file in filenames:
        if ".xml" in file:
            key = "80c90_"
            rename_xml = key+file

            mytree = ET.parse(mypath + file)
            myroot = mytree.getroot()

            # iterating throught the price values.
            for p11 in myroot.iter('filename'):
                # updates the price value
                p11.text = str(p11.text).replace("IMG", key+"IMG")
            # iterating throught the price values.
            for p12 in myroot.iter('path'):
                # updates the price value
                p12.text = str(p12.text).replace("IMG", key+"IMG")
            mytree.write(mypath + "bw/" + rename_xml)
