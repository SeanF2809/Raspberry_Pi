import os
import smtplib

email_address = 'python.sean1990@gmail.com'
rec_email_address = 'elfie.emz@gmail.com'
email_pass = 'deadpython'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()

	smtp.login(email_address, email_pass)

	subject = 'Cat at the door'
	body = 'Cat Dected at Door'

	msg = f'Subject: {subject}\n\n{body}'

	smtp.sendmail(email_address, rec_email_address, msg)
