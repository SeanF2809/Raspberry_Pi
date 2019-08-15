import pygame
import pygame.camera
import os
import smtplib
from email.message import EmailMessage
import imghdr

pygame.camera.init()

cam = pygame.camera.Camera("/dev/video2",(1024,800))
cam.start()

img = cam.get_image()
pygame.image.save(img,"/home/fergie/Pictures/test.jpg")

email_address = 'python.sean1990@gmail.com'
rec_email_address = 'elfie.emz@gmail.com'
email_pass = 'deadpython'

msg = EmailMessage()
msg['Subject'] = 'Cat at the Door'
msg['From'] = email_address
msg['To'] = rec_email_address
msg.set_content('Let the Cat in')

with open('/home/fergie/Pictures/test.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	

	smtp.login(email_address, email_pass)
	smtp.send_message(msg)
