from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from postmarker.core import PostmarkClient

postmark = PostmarkClient(server_token='92895c56-a7c3-4525-8a99-0bc297b6d354')
# send email function
def send_email():
    postmark.emails.send(
        From= "bethwpage@gmail.com",
        To= "wbeth.kamau@gmail.cm",
        Subject= "Testing",
        HtmlBody= "<strong>Hello</strong> new mail.",
        MessageStream="message"
    )
    
