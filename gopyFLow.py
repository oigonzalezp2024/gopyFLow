import codecs
import os
import time
from PIL import Image
from googletrans import Translator
from pytesseract import *

class GopyFlow(Translator):

    def setPytesseract(self, pytesseractPath:str)->None:
        self.pytesseract = pytesseract
        self.pytesseract.tesseract_cmd = pytesseractPath 

    def gopy(self, pathImages:str, pathDest:str)->None:
        images = os.listdir(pathImages)
        result = self.imagesToListText(images, pathImages)
        self.translateToListTextToSpa(images, result, pathDest)

    def imagesToListText(self, images:list, pathImages:str)->list:
        result = []
        for i in images:
            img = Image.open(pathImages+i)
            content= self.pytesseract.image_to_string(img)
            result.append(content)
        return result

    def translateToListTextToSpa(self, images:list, result:list, pathDest:str)->None:
        j=0
        for i in result:
            contentt = self.translate(i, dest="es")
            image = images[j]
            with codecs.open(pathDest, mode="a", encoding='utf-8') as f:
                f.write(str("## ")+str(image)+"\n"+str(i)+"\n"+ contentt.text+"\n\n")
            time.sleep(2)
            j+=1
