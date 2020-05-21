import smtplib

password = 'PASSWORD'


def sendMailTest():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('yifan.ding.official@gmail.com', password)

    subject = 'TEST1'
    body = 'test1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'yifan.ding.official@gmail.com',
        'yifan.ding@berkeley.edu',
        msg
    )
    print('HEY THE EMAIL HAS BEEN SENT')


sendMailTest()
