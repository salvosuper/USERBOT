from Telethon.events import message

#IT: Outgoing è per i messaggi che potranno essere eseguiti solo da voi stessi!
#EN: Outgoing is for messages that can only be executed by yourself!

@message(outgoing=True, pattern='[.]creator')
async def edit(e):
    await e.edit("creator: @salvouu", parse_mode="html")
