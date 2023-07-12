import smtplib
from django.core.mail import send_mail
from django.conf import settings


class CorreoElectronico:

    def enviarcorreo(tosend, subject, pmessage):
        fromsender = settings.EMAIL_HOST_USER

        try:
            send_mail(
                subject,
                pmessage,
                fromsender,
                [tosend],
                fail_silently=False,
            )
            print("Successfully sent email")
        except smtplib.SMTPException as e:
            error_code = e.smtp_code
            error_message = e.smtp_error
            print("Error sent email {}-{}".format(error_code,error_message))
            pass
