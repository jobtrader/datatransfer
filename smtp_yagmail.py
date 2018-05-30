# Send mail via simple mail transfer protocol.
def smtp(gmail_username, gmail_password, to_email_addres, message, server_name='smtp.gmail.com', port=587):
    import smtplib  # Import smtp module.

    mail_server = smtplib.SMTP(server_name, port)   # Establish mail instance.
    mail_server.ehlo()  # Identify yourself to an ESMTP server.
    try:
        mail_server.starttls() # Put the SMTP connection in TLS.
    except Exception as e:
        return e
    try:
        mail_server.login(gmail_username, gmail_password) # Log in on an SMTP server that requires authentication.
    except Exception as e:
        return e
    try:
        mail_server.sendmail(gmail_username, to_email_addres, message) # Send mail.
    except Exception as e:
        return e
    mail_server.close() # Close the connection.

# Sending email using YAGMAIL.
def yag_mail(gmail_username, fake_alias, gmail_password, to_email, subject, body):
    import yagmail # Import yagmail module

    mail = yagmail.SMTP({gmail_username : fake_alias}, gmail_password) # Establis mail instance.
    try:
        mail.send(to_email, subject, body) # Send mail.
    except Exception as e:
         return e