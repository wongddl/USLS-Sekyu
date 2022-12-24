from sendgrid.helpers.mail import HtmlContent, Mail
import openai
from utils import gsheets,utilhtml

openai.api_key = "{openai_key}"

def emailmessage(message_content,random_code):
    emailmessage = Mail(
                    from_email=(gsheets.SENDGRID_EMAIL),
                    to_emails=message_content,
                    subject='Verify your server email',
                    html_content= HtmlContent(utilhtml.email_message.format(message_content,random_code,message_content)))
    return emailmessage

def generate_image_with_openai(description: str) -> str:
    response = openai.Image.create(
        prompt=description,
        model="image-alpha-001",
        size="1024x1024",
        response_format="url"
        )  
    return response["data"][0]["url"]


def generate_text_with_openai(description: str) -> str:
    response = openai.Completion.create(
        model="text-davinci-003", 
        prompt=description, 
        max_tokens=1024
        )
    return response['choices'][0]['text']
