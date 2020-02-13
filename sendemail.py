import smtplib
#server = smtplib.SMTP('smtp.gmail.com', 587)
smtp = smtplib.SMTP('smtp.gmail.com',587)
smtp.starttls()
#Next, log in to the server
smtp.login("qa.trainer2017", "***")

#Send the mail
msg = """Test mail from python Hello!""" # The /n separates the message from the headers
smtp.sendmail("qa.trainer2017@gmail.com", "trainer.raji@gmail.com", msg)

