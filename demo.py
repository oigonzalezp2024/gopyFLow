
from gopyFLow import GopyFlow

gopyFlow = GopyFlow()

pytesseractPath = str("C:/Program Files/Tesseract-OCR/tesseract.exe")
pathImages = str("./images/")
pathDest = str("./translation/translation.md")

gopyFlow.setPytesseract(pytesseractPath)
gopyFlow.gopy(pathImages, pathDest)
