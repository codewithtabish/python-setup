import easyocr
import requests
from io import BytesIO
from PIL import Image

def extract_text_from_image_url(image_url):
    # Initialize the EasyOCR Reader with the language you want (default: English)
    reader = easyocr.Reader(['en'])  # You can add more languages if needed
    
    # Fetch the image from the URL
    response = requests.get(image_url)
    
    if response.status_code == 200:
        # Convert the image to a format that EasyOCR can work with
        img = Image.open(BytesIO(response.content))
        
        # Perform OCR on the image
        result = reader.readtext(img)
        
        # Combine all the text from the result
        extracted_text = ' '.join([text[1] for text in result])
        
        return extracted_text
    else:
        return None
