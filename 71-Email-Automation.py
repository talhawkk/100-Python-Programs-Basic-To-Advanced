import smtplib
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
#point to be noted google allow ni krta aeisay kisi third chez ko access krne ki isi google account pr ja k app password create krna prta or wo lagama prta phir chalay gay
server.login("talhawkk@gmail.com","dsss ssfs sfss ssss")
server.sendmail("talhawkk@gmail.com","talhawk6@gmail.com","this is send by automated bot")
