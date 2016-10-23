import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587, "arbuzovfp@gmail.com", timeout=120)
server.starttls()
server.login("arbuzovfp@gmail.com", "CShse2016")

msg = "YOUR MESSAGE!"
server.sendmail("arbuzovfp@gmail.com", "ArbuzovFP@yandex.ru", msg)
server.quit()