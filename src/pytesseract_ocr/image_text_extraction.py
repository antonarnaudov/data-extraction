from PIL import Image
import pytesseract

# Paths to the uploaded images
prefix = "/Users/c-aarnau/Downloads/pavkata"
image_paths = [
    f"{prefix}/viber_image_2024-11-29_14-39-46-236.png",
    f"{prefix}/viber_image_2024-11-29_14-39-45-735.png",
    f"{prefix}/viber_image_2024-11-29_14-28-41-613.png",
]

print('"""')
# Extract text from images
# extracted_text = ""


for image_path in image_paths:
    image = Image.open(image_path)
    print(pytesseract.image_to_string(image))

    # extracted_text += pytesseract.image_to_string(image) + "\n\n"

print('"""')

# print(extracted_text)
