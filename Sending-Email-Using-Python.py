import smtplib
fromaddr="youraccount@gmail.com"
toaddr="recieveraccount9711@gmail.com"
message="hello bitches"
password="yourpassword"
server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(fromaddr,password)
server.sendmail(fromaddr,toaddr,message)
server.quit()
