from sendgrid.helpers.mail import HtmlContent, Mail

from utils import gsheets,utilhtml


def emailmessage(message_content,random_code):
    emailmessage = Mail(
                    from_email=(gsheets.SENDGRID_EMAIL),
                    to_emails=message_content,
                    subject='Verify your server email',
                    html_content= HtmlContent(utilhtml.email_message.format(message_content,random_code,message_content)))
    return emailmessage