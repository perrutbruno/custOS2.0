import smtplib

#Old method we used to alert us. Now we're using rocketChat to alert us, but i'll keep the object safe :) and won't delete it.
class Mailer:
    def __init__(self, smtp_server, login, password, receiver_email):
        self.smtp_server = smtp_server
        self.login = login
        self.password = password
        self.receiver_email = receiver_email

    def email_send(self, message):
        smtp_server = self.smtp_server
        login = self.login
        password = self.password
        receiver_email = self.receiver_email
        port = 25
        sender = login
        receiver = receiver_email

        message = f'''\\
From: {login}
To: {receiver_email}
Subject: custOS Mail ALERT!
\nBelow are some warning points to the DevOps team pay attention about

{message}


This message was generated automatically by the custOS script.'''
            # Send your message with credentials specified above
        try:
            with smtplib.SMTP(smtp_server, port) as server:

                server.login(login, password)

                server.sendmail(sender, [receiver], message)

        except Exception as e:
            print(e)
