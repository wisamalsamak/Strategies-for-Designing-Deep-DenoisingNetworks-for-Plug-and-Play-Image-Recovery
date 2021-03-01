# coding:utf-8
import os
from PIL import Image

# bmp to jpg
def bmpToJpg(file_path):
    for fileName in os.listdir(file_path):
        # print(fileName)
        newFileName = str(fileName.split('.')[0])+".jpg"

        #print(newFileName)
        im = Image.open(file_path+"\\"+fileName)
        if im.mode in ("RGBA", "P"):
            im = im.convert("RGB")
        im.save(file_path+"\\"+newFileName)


# Delete the original bitmap
def deleteImages(file_path, imageFormat):
    command = "del "+file_path+"\\*."+imageFormat
    os.system(command)


def main():
    dir_name = r"C:\Users\wisam\Downloads\pristine_images"
    bmpToJpg(dir_name)
    import os




    test = os.listdir(dir_name)

    for item in test:
        if item.endswith(".bmp"):
            os.remove(os.path.join(dir_name, item))


if __name__ == '__main__':
    main()
