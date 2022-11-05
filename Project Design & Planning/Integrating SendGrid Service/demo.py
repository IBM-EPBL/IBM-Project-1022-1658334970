import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(api_key= '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' )
from_email = Email("chinnukool72@gmail.com")
to_email = To("sarika.19102@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
