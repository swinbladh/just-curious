# just-curious

A collection of things I've been curious about.

## analyze-pdf

Analyzing and extracting text from PDFs. Useful for data mining.

The script contains two pathways:

1. Reading "well structured" PDFs that doesn't require Optical Character Recognition (OCR)
2. Reading PDFs that require OCR

Packages used:

-   pdfminer.six: reading text from well structured PDFs
-   pdf2image: converting each page of a PDF to an image. Needed since OCR requires image files.
-   PIL: Python Image Library, used to process images
-   pytesseract: Wrapper for Google's tesseract engine. Provides OCR capabilities.
