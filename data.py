from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("π₯ πππππ πΆπππππππππ πππππππ π₯", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="π  Return Home π ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("β¨ Bot Status and More Bots β¨", url="https://t.me/MetraVoid")],
        [
            InlineKeyboardButton("How to Use β", callback_data="help"),
            InlineKeyboardButton("πͺ About πͺ", callback_data="about")
        ],
        [InlineKeyboardButton("β₯ More Amazing bots β₯", url="https://t.me/MetraVoid")],
    ]

    START = """
Hey {}

Welcome to {}

If you don't trust this bot, 
1) Stop Reading This Message
2) Delete This Chat

Still reading?
You can use me to generate pyrogram (even version 2) and telethon string session. Use below buttons to learn more !

By @MetraVoid
    """

    HELP = """
β¨ **Available Commands** β¨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @MetraVoid

Source Code : [Click Here](https://github.com/StarkBotsIndustries/StringSessionBot)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

Developer : @Ashmit_xD
    """
