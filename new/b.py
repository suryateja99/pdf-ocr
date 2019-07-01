from PIL import Image
import pytesseract
img=['image/1.png','image/2.png','image/3.png','image/4.png']
p=""
for i in img:
	p+=str(pytesseract.image_to_string(Image.open(i)))
	print(i)
print(p)