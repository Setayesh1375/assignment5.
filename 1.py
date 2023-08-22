import qrcode
name=input("please enter your name ")
phone_number=input("please enter your phone number ")
x = qrcode.make("name | phone number")
x.save("my_first_qrcode.png")