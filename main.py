# pip install pyqrcode
import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
link = "https://www.youtube.com/"

# Generate QR code
url = pyqrcode.create(link)

# Create and save the png file naming "myqr.png"
url.svg("myyoutube.svg", scale=8)
