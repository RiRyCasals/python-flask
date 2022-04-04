import os
import qrcode

qr = qrcode.QRCode(
    box_size=4,
    border=8,
    version=12,
    error_correction=qrcode.constants.ERROR_CORRECT_Q
)
qr.add_data('https://kujirahand.com')
qr.make()
img = qr.make_image()
img.save(os.path.dirname(__file__) + '/qrcode2.png')
print('ok')
