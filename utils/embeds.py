import discord
from discord.ui import Button, View


def embed_admission():
    admission_msg=discord.Embed(title="Welcome to Rektikano Esports League", description="""
    To gain further access and perks to our discord server, follow the steps below!

    __Steps:__
    1.) Click the **" <:verify1:1047737368947458068><:verify2:1047737742894845962> "** button below.
    2.) <@1024581083116884029> will automatically respond and DM you.
    3.) Type in your valid **USLS email address**. 
    ||s<id_number>@usls.edu.ph||
    4.) A **unique code** to be sent to your email.
    5.) Reply the given **code**.
    6.) You will receive access through <@&1026435520726831115> role!
        """, color=0x0b3434)
    admission_msg.set_image(url='https://media.discordapp.net/attachments/1025354287057997875/1027531331883782154/header.png')
    admission_msg.set_thumbnail(url='https://media.discordapp.net/attachments/1025354287057997875/1025786803753603092/287898692_519819426558916_288893622064928495_n.jpg')
    admission_msg.set_footer(text="Verification process is fully automated. Contact Moderators if verification process doesn't work.",icon_url="https://media.discordapp.net/attachments/1025354287057997875/1027531902762094592/287898692_519819426558916_288893622064928495_n-modified.png")
    
    return admission_msg


def embed_message():
    # 1
    tabasd=discord.Embed(title="Welcome to Rektikano Esports League", description="""
    This verification process is for **USLS students** only.

    __Steps:__
    1.) Click the **" <:verify1:1047737368947458068><:verify2:1047737742894845962> "** button below.
    2.) <@1024581083116884029> will automatically respond and DM you.
    3.) Type in your valid **USLS email address**. 
    ||s<id_number>@usls.edu.ph||
    4.) A **unique code** to be sent to your email.
    5.) Reply the given **code**.
    6.) You will receive access through @Students role!
        """, color=0x0b3434)
    tabasd.set_image(url='https://media.discordapp.net/attachments/1025354287057997875/1027531331883782154/header.png')
    tabasd.set_thumbnail(url='https://media.discordapp.net/attachments/1025354287057997875/1025786803753603092/287898692_519819426558916_288893622064928495_n.jpg')
    tabasd.set_footer(text="Verification process is fully automated. Contact Moderators if verification process doesn't work.",icon_url="https://media.discordapp.net/attachments/1025354287057997875/1027531902762094592/287898692_519819426558916_288893622064928495_n-modified.png")
    
    # 2
    embedemail=discord.Embed(title="Type in your valid USLS email address", description="""
Example:
`s123456@usls.edu.ph`
    """, color=0xffffff)
    embedemail.set_footer(text="This message will delete in 30 seconds")
    
    #3
    embedverfcode=discord.Embed(title="Type in your Verification Code", description="""
Example:
`987654`
    """, color=0xffffff)
    embedverfcode.set_footer(text="This message will delete in 30 seconds.")

    #4
    verified_message = discord.Embed(title='Welcome to Rektikano Esports League', description = f'''
    You are now verified on **Rektikano Esports League** discord server.

    To get you started, head over to:
    <#1024652601368780900> for Navigation guide of our server.
    or drop by at:
    <#1024915125632770089> for our other Rektikano Esports League social media platforms.
    ''', color = 0x0b3434)
    verified_message.set_image(url='https://media.discordapp.net/attachments/1025354287057997875/1030941561858568332/verified.png')
    verified_message.set_thumbnail(url='https://media.discordapp.net/attachments/1025354287057997875/1025786803753603092/287898692_519819426558916_288893622064928495_n.jpg')
    verified_message.set_footer(text="Verification process is fully automated. Contact Moderators if verification process doesn't work.",
                            icon_url="https://media.discordapp.net/attachments/1025354287057997875/1027531902762094592/287898692_519819426558916_288893622064928495_n-modified.png")
    
    #5
    email_message = discord.Embed(title='📨 Email Sent',description='**Verification code** has been sent to your school Email Address.', color = 0x0b3434)
    email_message.set_footer(text="Check your spam folders if the email is not at your inbox.")

    return tabasd,embedemail,embedverfcode,verified_message,email_message

def embed_sent_button():
    emailsent = Button(label="📧 Gmail", url='https://gmail.com', style=discord.ButtonStyle.grey)
    view = View()
    view.add_item(emailsent)
    return view

def embed_invalid():
    embed_invalid_input = discord.Embed(title='Invalid Input', color = 0xFF0000)
    embed_invalid_input.set_footer(text="This message will delete in 5 seconds.")
    embed_invalid_code = discord.Embed(title='Invalid Code', color = 0xFF0000)
    embed_invalid_code.set_footer(text="This message will delete in 5 seconds.")
    return embed_invalid_input,embed_invalid_code