from email.mime.text import MIMEText
# from email.header import Header
import smtplib


def send_email(message, from_addr, password, to_addr, smtp_server):
    msg = MIMEText("New user:" + message, "plain", "utf-8")
    # msg["From"] = Header(app.config['MAIL_USERNAME'], "utf-8")
    # msg["To"] = Header(app.config['FLASKY_SENDER'], "utf-8")
    # msg["Subject"] = Header(app.config['FLASKY_MAIL_SUBJECT_PREFIX'], "utf-8")
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()