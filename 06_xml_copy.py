from os import walk
import xml.etree.ElementTree as ET

mypath = "dataset/RESIZE/"
# checked = ["IMG_20201208_113851.xml", "IMG_20201208_113858.xml","IMG_20201208_113904.xml"]
checked = []

basefile = "re_20210223_132743(001)_No.0.xml"
base_path = mypath + basefile


def load_base_xml(mytree):
    output = mytree.getroot()
    return output


for (_, _, filenames) in walk(mypath):
    for file in filenames:
        if (".jpg" in file) and (file not in checked):
            pfx_file = (file[:-4])
            if pfx_file not in basefile:
                mytree = ET.parse(base_path)
                myroot = load_base_xml(mytree)

                # iterating throught the price values.
                for p11 in myroot.iter('filename'):
                    # updates the price value
                    p11.text = file
                # iterating throught the price values.
                for p12 in myroot.iter('path'):
                    # updates the price value
                    p12.text = str(p12.text).replace(basefile[:-4], pfx_file)
                mytree.write(mypath + pfx_file + ".xml")
