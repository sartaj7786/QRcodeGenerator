import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("\nCoding with Sattar")
qr.png("mycode.png",scale=8)

d=decode(Image.open("myCode.png"))
print(d[0].data.decode("ascii"))
