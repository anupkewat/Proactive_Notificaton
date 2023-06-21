import smtplib
import ssl
from dotenv import load_dotenv

from email.message import EmailMessage
import os

def send_proactive_email(notifications, messages, email_recipients):
    load_dotenv()
    print("Sending Email..")
    email_sender = os.getenv("EMAIL_SENDER")
    email_password = os.getenv("PASSWORD_SENDER")
    # Set the subject and body of the email
    
    subject = 'Proactive Notification - LinkedIn '
    body = f"""You have : {notifications} messages and {messages} notificatons.
    """

    em = EmailMessage()


    em['From'] = email_sender
    em['To'] = ",".join(email_recipients)
    em['Subject'] = subject
    em.set_content(body)
    sending_to =  em['To']
    print( f"sending email update to : {sending_to}")

    # Adding SSL security
    context = ssl.create_default_context()

    # Log in and send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_recipients, em.as_string())
        print("Successfully Sent Mail Update")
    except smtplib.SMTPException as e:
        print("Unable to send email:", str(e))



load_dotenv()
