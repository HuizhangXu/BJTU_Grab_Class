from PIL import Image
import pytesser
import pytesseract

image = Image.open('test.jpg')

print(pytesseract.image_file_to_string('test.jpg'))
print(pytesseract.image_to_string(image))
