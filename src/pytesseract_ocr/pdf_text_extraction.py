import fitz  # PyMuPDF
from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf(path):
    # Store extracted text
    extracted_text = ""

    # Load the PDF
    doc = fitz.open(path)

    for page_num in range(len(doc)):
        # Render the page as an image
        page = doc.load_page(page_num)
        pix = page.get_pixmap(dpi=300)
        img_path = f"page_{page_num + 1}.png"
        pix.save(img_path)

        # Perform OCR using Tesseract
        text = pytesseract.image_to_string(img_path)
        extracted_text += f"--- Page {page_num + 1} ---\n{text}\n"

    return extracted_text

# Example usage
pdf_path = "/Users/c-aarnau/Downloads/Варна.pdf"
text = extract_text_from_pdf(pdf_path)
print(text)
