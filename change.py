from PIL import Image, ImageFilter, ImageEnhance
import os

#paste in your own image in the ()
image = Image.open('me2.jpg')
image.rotate(90).save('me2.jpg')
#converts the image color to black and white
image.convert(mode = 'L').save('me2.jpg')
image.show()
image.save('me2.png')
#makes the image cleanner
enh = ImageEnhance.Contrast(image)
enh.enhance(1.3).show("80% more contrast")
#blurs the image
boxImage = image.filter(ImageFilter.BoxBlur(5))
boxImage.show()