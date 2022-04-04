import os
import qrcode

img = qrcode.make('https://kujirahand.com')
img.save(os.path.dirname(__file__) + '/qrcode.png')
print('ok')
