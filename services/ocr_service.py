from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)

        img = img.convert('L') 
        img = img.filter(ImageFilter.SHARPEN)
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2) 

        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        print(f"❌ OCR failed: {e}")
        return ""