import json
import glob
import base64
from labelme import utils
from PIL import Image
import copy
from io import BytesIO

dir_images = "../images/type_1/"
file_base = "frame_2021-02-12_194659_IN4.json"
base = dir_images + file_base
with open(base, "r") as f:
    data = json.load(f)


def _check_image_height_and_width(imageData, imageHeight, imageWidth):
    img_arr = utils.img_b64_to_arr(imageData)
    if imageHeight is not None and img_arr.shape[0] != imageHeight:
        imageHeight = img_arr.shape[0]
    if imageWidth is not None and img_arr.shape[1] != imageWidth:
        imageWidth = img_arr.shape[1]
    return imageHeight, imageWidth


images_path = glob.glob(dir_images + "*.jpg")
for p in images_path[:30]:
    if file_base[:-4] not in p:
        temp_data = copy.deepcopy(data)
        im = Image.open(p)
        shape = im.size
        imageHeight = shape[0]
        imageWidth = shape[1]

        buffered = BytesIO()
        im.save(buffered, format="JPEG")
        imageData = base64.b64encode(buffered.getvalue())
        imageHeight, imageWidth = _check_image_height_and_width(
            imageData, imageHeight, imageWidth
        )
        split_path = temp_data["imagePath"].split("\\")
        temp_data["imagePath"] = "\\".join(split_path[:-1]) + "\\" + p.split("\\")[-1]
        temp_data["imageData"] = str(imageData)[2:-1]

        try:
            with open(p.replace(".jpg", ".json"), "w") as f:
                json.dump(temp_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            raise e
