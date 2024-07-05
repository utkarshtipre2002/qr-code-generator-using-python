import qrcode
import image

qr = qrcode.QRCode(
    version=15,
    box_size=10,  # size of the box where qr code will be displayed
    border=5,  # it is the white part of the image 
)

data = "https://www.youtube.com/watch?v=4e-I6IDBgK0&list=RDGMEMCMFH2exzjBeE_zAHHJOdxgVM6J9okctVu58&index=2"

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('test.png')
