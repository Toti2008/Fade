from http.server import BaseHTTPRequestHandler, HTTPServer
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

request = None
sender = None
sender_pass = None
Reciver = None
Message = None
Smtpserv = None
Smtp_Port = None
Spam___Y_or_N_ = None

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global request, sender, sender_pass, Reciver, Message, Smtpserv, Smtp_Port, Spam___Y_or_N_
    messagetosend = bytes('Email Spam Client V0.3',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    request = self.requestline
    request = request[5 : int(len(request)-9)]
    if request == 'start':
      sender = input('Sender')
      sender_pass = input('password ')
      Reciver = input('Send to ? ')
      Message = input('Message')
      Smtpserv = input('Smtp Server? ')
      Smtp_Port = input('Smtp Port? ')
      Spam___Y_or_N_ = input('Spam Y or N? ')
      if Spam___Y_or_N_ == 'Y':
        while Spam___Y_or_N_ == 'Y':
          email_sender = sender
          email_receiver = Reciver
          subject = Message
          msg = MIMEMultipart()
          msg['From'] = email_sender
          msg['To'] = email_receiver
          msg['Subject']= subject
          body = Message
          msg.attach(MIMEText(body, 'plain'))

          text = msg.as_string()
          connection = smtplib.SMTP(Smtpserv, Smtp_Port)
          connection.starttls()
          connection.login(email_sender, sender_pass)
          connection.sendmail(email_sender, email_receiver, text )
          connection.quit()
          if request == 'stop':
            Spam___Y_or_N_ = 'N'
            print('spam stopped')
          time.sleep(5)
      if Spam___Y_or_N_ == 'N':
        email_sender = sender
        email_receiver = Reciver
        subject = Message
        msg = MIMEMultipart()
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject']= subject
        body = Message
        msg.attach(MIMEText(body, 'plain'))

        text = msg.as_string()
        connection = smtplib.SMTP(Smtpserv, Smtp_Port)
        connection.starttls()
        connection.login(email_sender, sender_pass)
        connection.sendmail(email_sender, email_receiver, text )
        connection.quit()
    return


server_address_httpd = ('127.0.0.1',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
httpd.serve_forever()
