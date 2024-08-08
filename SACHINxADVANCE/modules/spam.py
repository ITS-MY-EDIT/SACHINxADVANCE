## Copy Paster Must Give Credit...
## @SACHINxADVANCE_V2

import asyncio
from random import choice
from telethon import events, functions, types
from SACHINxADVANCE.data import GROUP, PORMS
from config import SACHIN0, SACHIN1, SACHIN2, SACHIN3, SACHIN4, SACHIN5, SACHIN6, SACHIN7, SACHIN8, SACHIN9, SUDO_USERS, CMD_HNDLR as hl

async def gifspam(event, message):
    try:
        await event.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=message.media.document.id,
                    access_hash=message.media.document.access_hash,
                    file_reference=message.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

async def send_messages(event, message, count):
    for _ in range(count):
        if event.reply_to_msg_id:
            await event.reply(message)
        else:
            await event.client.send_message(event.chat_id, message)
        await asyncio.sleep(0.2)

async def send_media(event, message, count):
    for _ in range(count):
        message = await event.client.send_file(event.chat_id, message, caption=message.text)
        await gifspam(event, message)
        await asyncio.sleep(0.2)

@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
async def spam(event):
    if event.sender_id in SUDO_USERS:
        command = event.text.split(" ", 2)
        reply_message = await event.get_reply_message()
        try:
            count = int(command[1])
            if len(command) == 3:
                await send_messages(event, command[2], count)
            elif reply_message.media:
                await send_media(event, reply_message, count)
            elif reply_message.text:
                await send_messages(event, reply_message.text, count)
            else:
                await event.reply(f"⚔️ **ᴜsᴀɢᴇ:**\n  » {hl}spam 04 ᴊᴀʀᴠɪs\n  » {hl}spam 04 <ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ>\n\n**ᴛᴏ ᴅᴏ sᴘᴀᴍ ᴡɪᴛʜ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀ ᴜsᴇʀ:**\n  » {hl}spam 04 ᴊᴀʀᴠɪs <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>")
        except (IndexError, ValueError):
            await event.reply(f"⚔️ **ᴜsᴀɢᴇ:**\n  » {hl}spam 04 ᴊᴀʀᴠɪs\n  » {hl}spam 04 <ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ>\n\n**ᴛᴏ ᴅᴏ sᴘᴀᴍ ᴡɪᴛʜ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀ ᴜsᴇʀ:**\n  » {hl}spam 04 ᴊᴀʀᴠɪs <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)

@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
async def pspam(event):
    if event.sender_id in SUDO_USERS:
        if event.chat_id in GROUP:
            await event.reply("➪ ᴛʜɪs ɢʀᴏᴜᴘ ɪs ɪɴ sᴜʀᴠɪʟʟᴀɴᴄᴇ ᴏғ ᴊᴀʀᴠɪs sᴏ ʜᴇʀᴇ ᴘsᴘᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴡᴏʀᴋ...")
        else:
            try:
                count = int(event.text.split(" ", 2)[1])
                porn = choice(PORMS)
                await send_media(event, porn, count)
            except (IndexError, ValueError):
                await event.reply(f"🔞 **Usage:**  {hl}pspam 04")
            except Exception as e:
                print(e)
