from pdfminer.high_level import extract_text
from pdf2image import convert_from_path
from PIL import Image
import os
import pytesseract


class PDF:
    def __init__(self, pdf, outputFile, ocr):
        self.pdf = pdf
        self.outputFile = outputFile
        self.ocr = ocr
        self.imageStore = "./images"

    def extract(self):
        # Extracting text from any PDF

        text = ""
        if self.ocr:
            text = self.ocrExtract()
        else:
            text = self.textExtract()

        self.writeToTextFile(text)
        return None

    def textExtract(self):
        # Works well with well structured PDFs
        # Useless with scanned PDFs
        return extract_text(self.pdf)

    def ocrExtract(self):
        # When text cannot be read from PDF directly, OCR is needed
        self.pdfToImage()
        text = self.readingTextFromImage()
        self.deletingImages()

        return text

    def pdfToImage(self):
        images = convert_from_path(self.pdf)
        for image in range(len(images)):
            images[image].save(f"{self.imageStore}/page_{str(image)}.jpg", "JPEG")

        return None

    def readingTextFromImage(self):
        images = os.listdir(self.imageStore)

        pdfText = ""
        for image in range(len(images)):
            filename = f"{self.imageStore}/page_{str(image)}.jpg"
            imageOpen = Image.open(filename)
            imageToString = pytesseract.image_to_string(imageOpen)
            text = str(imageToString).replace("-\n", "")

            pdfText += f"\n{text}"

        return pdfText

    def deletingImages(self):
        files = os.listdir(self.imageStore)

        for file in files:
            os.remove(f"{self.imageStore}/{file}")

        return None

    def writeToTextFile(self, text):
        with open(self.outputFile, "w") as output:
            output.write(text)

        return None


if __name__ == "__main__":
    # pdfFile = "ocrTest.pdf"
    pdfFile = "textTest.pdf"
    ocr = False
    outputFile = "text.txt"
    PDF(pdfFile, outputFile, ocr).extract()
