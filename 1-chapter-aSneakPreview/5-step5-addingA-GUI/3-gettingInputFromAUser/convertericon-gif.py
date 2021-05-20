from PIL import Image

img = Image.open('pythonImgIco.ico')
img.show()

img.save('pythonImgIco.gif')