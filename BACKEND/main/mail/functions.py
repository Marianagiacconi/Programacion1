from flask import current_app, render_template
from flask_mail import Message
from smtplib import SMTPException

def sendMail(to, subject, template, **kwargs):
    # Obtener mailsender desde current_app
    mailsender = current_app.extensions['mail']
    
    # Configuración del mail
    msg = Message(subject, sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=to)
    
    try:
        # Creación del cuerpo del mensaje
        msg.body = render_template(template + '.txt', **kwargs)
        msg.html = render_template(template + '.html', **kwargs)
        
        # Envío del mail
        result = mailsender.send(msg)
    except SMTPException as e:
        print(str(e))
        return "Mail delivery failed"
    
    return True
