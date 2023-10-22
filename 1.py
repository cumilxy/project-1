from PIL import Image, ImageFilter
with Image.open('ponpon.jpg')as o:
    o.show()
    photo2 = o.convert('L')
    photo2.show()
    photo3 = o.filter(ImageFilter.BLUR)
    photo3.show()
    
    o.show()