## Copy Paster Must Give Credit...
## @SACHINxADVANCE_V2

import asyncio
from random import choice
from telethon import events
from config import SACHIN0, SACHIN1, SACHIN2, SACHIN3, SACHIN4, SACHIN5, SACHIN6, SACHIN7, SACHIN8, SACHIN9, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from SACHINxADVANCE.data import RAID, REPLYRAID, SACHIN, MRAID, SRAID, QRAID

REPLY_RAID = []

# Helper function to get user entity from a message
async def get_user_entity(e):
    if len(e.text.split()) > 2:
        return await e.client.get_entity(e.text.split()[2])
    if e.reply_to_msg_id:
        reply_msg = await e.get_reply_message()
        return await e.client.get_entity(reply_msg.sender_id)
    return None

# Helper function to handle exceptions
async def handle_exception(e, module_name):
    if not (e.reply_to_msg_id or len(e.text.split()) > 2):
        await e.reply(f"**ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ**: {module_name}\n  » {hl}{module_name.lower()} <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}{module_name.lower()} <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

# Function to execute raid
async def execute_raid(e, uid, first_name, counter, raid_list):
    username = f"[{first_name}](tg://user?id={uid})"
    for _ in range(counter):
        reply = choice(raid_list)
        caption = f"{username} {reply}"
        await e.client.send_message(e.chat_id, caption)
        await asyncio.sleep(0.1)

# Event handler for different raid types
async def raid_handler(e, raid_list, module_name):
    if e.sender_id in SUDO_USERS:
        try:
            entity = await get_user_entity(e)
            if entity:
                uid = entity.id
                first_name = entity.first_name
                counter = int(e.text.split()[1])
                if uid in SACHIN:
                    await e.reply("ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴛʜᴇ ᴄʀᴇᴀᴛᴏʀ ᴏғ ᴛʜɪs ᴘʀᴏᴊᴇᴄᴛ sᴏᴜʀᴄᴇ.")
                elif uid == OWNER_ID:
                    await e.reply("ᴋɪᴅᴢᴢ😂 ᴏᴡɴᴇʀ ʜᴀɪ ʏᴇ ᴍᴇʀᴀ ʙᴀʜᴜᴛ ᴍᴀʀᴇɢᴀ...")
                elif uid in SUDO_USERS:
                    await e.reply("ᴛʜɪs ᴘᴇʀsᴏɴ ᴀʟsᴏ ʜᴀᴠᴇ ᴀʙɪʟɪᴛɪᴇs ᴛᴏ ᴜsᴇ ᴍᴇ sᴏ ɪ ᴄᴀɴᴛ ɢᴏ ᴀɢᴀɪɴsᴛ ᴛʜᴇᴍ...")
                else:
                    await execute_raid(e, uid, first_name, counter, raid_list)
            else:
                await handle_exception(e, module_name)
        except (IndexError, ValueError, NameError):
            await handle_exception(e, module_name)
        except Exception as ex:
            print(ex)

# Event handler for reply raid
async def reply_raid_handler(e, module_name):
    if e.sender_id in SUDO_USERS:
        try:
            entity = await get_user_entity(e)
            if entity:
                user_id = entity.id
                if user_id in SACHIN:
                    await e.reply("ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴛʜᴇ ᴄʀᴇᴀᴛᴏʀ ᴏғ ᴛʜɪs ᴘʀᴏᴊᴇᴄᴛ sᴏᴜʀᴄᴇ.")
                elif user_id == OWNER_ID:
                    await e.reply("ᴋɪᴅᴢᴢ😂 ᴏᴡɴᴇʀ ʜᴀɪ ʏᴇ ᴍᴇʀᴀ ʙᴀʜᴜᴛ ᴍᴀʀᴇɢᴀ....")
                elif user_id in SUDO_USERS:
                    await e.reply("ᴛʜɪs ᴘᴇʀsᴏɴ ᴀʟsᴏ ʜᴀᴠᴇ ᴀʙɪʟɪᴛɪᴇs ᴛᴏ ᴜsᴇ ᴍᴇ sᴏ ɪ ᴄᴀɴᴛ ɢᴏ ᴀɢᴀɪɴsᴛ ᴛʜᴇᴍ...")
                else:
                    check = f"{user_id}_{e.chat_id}"
                    if check not in REPLY_RAID:
                        REPLY_RAID.append(check)
                    await e.reply("» ʀᴇᴘʟʏ ʀᴀɪᴅ ʜᴀs ʙᴇᴇɴ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴏɴ ᴛʜɪs ɢᴜʏ ✅")
            else:
                await handle_exception(e, module_name)
        except NameError:
            await handle_exception(e, module_name)

# Event handler for disabling reply raid
async def disable_reply_raid_handler(e, module_name):
    if e.sender_id in SUDO_USERS:
        try:
            entity = await get_user_entity(e)
            if entity:
                check = f"{entity.id}_{e.chat_id}"
                if check in REPLY_RAID:
                    REPLY_RAID.remove(check)
                await e.reply("» ʀᴇᴘʟʏ ʀᴀɪᴅ ʜᴀs ʙᴇᴇɴ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴏɴ ᴛʜɪs ɢᴜʏ ✅")
            else:
                await handle_exception(e, module_name)
        except NameError:
            await handle_exception(e, module_name)

# Adding event handlers
@SACHIN0.on(events.NewMessage(incoming=True, pattern=rf"\%sraid(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=rf"\%sraid(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=rf"\%sraid(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=rf"\%srraid(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=rf"\%sraid(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=rf"\%sraid(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=rf"\%sraid(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=rf"\%sraid(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=rf"\%sraid(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=rf"\%sraid(?: |$)(.*)" % hl))
async def raid_event(e):
    await raid_handler(e, RAID, "Raid")

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
async def reply_raid_event(event):
    check = f"{event.sender_id}_{event.chat_id}"
    if check in REPLY_RAID:
        await asyncio.sleep(0.1)
        await event.client.send_message(
            entity=event.chat_id,
            message=choice(REPLYRAID),
            reply_to=event.message.id,
        )

@SACHIN0.on(events.NewMessage(incoming=True, pattern=rf"\%srraid(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=rf"\%srraid(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=rf"\%srraid(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=rf"\%srraid(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=rf"\%srraid(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=rf"\%srraid(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=rf"\%srraid(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=rf"\%srraid(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=rf"\%srraid(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=rf"\%srraid(?: |$)(.*)" % hl))
async def rraid_event(e):
    await reply_raid_handler(e, "ReplyRaid")

@SACHIN0.on(events.NewMessage(incoming=True, pattern=rf"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=rf"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=rf"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=rf"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=rf"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=rf"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=rf"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=rf"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=rf"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=rf"\%sdrraid(?: |$)(.*)" % hl))
async def drraid_event(e):
    await disable_reply_raid_handler(e, "DRreplyRaid")

@SACHIN0.on(events.NewMessage(incoming=True, pattern=rf"\%smraid(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=rf"\%smraid(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=rf"\%smraid(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=rf"\%smraid(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=rf"\%smraid(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=rf"\%smraid(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=rf"\%smraid(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=rf"\%smraid(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=rf"\%smraid(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=rf"\%smraid(?: |$)(.*)" % hl))
async def mraid_event(e):
    await raid_handler(e, MRAID, "MRaid")

@SACHIN0.on(events.NewMessage(incoming=True, pattern=rf"\%ssraid(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=rf"\%ssraid(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=rf"\%ssraid(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=rf"\%ssraid(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=rf"\%ssraid(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=rf"\%ssraid(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=rf"\%ssraid(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=rf"\%ssraid(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=rf"\%ssraid(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=rf"\%ssraid(?: |$)(.*)" % hl))
async def sraid_event(e):
    await raid_handler(e, SRAID, "SRaid")

@SACHIN0.on(events.NewMessage(incoming=True, pattern=rf"\%sqraid(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=rf"\%sqraid(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=rf"\%sqraid(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=rf"\%sqraid(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=rf"\%sqraid(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=rf"\%sqraid(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=rf"\%sqraid(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=rf"\%sqraid(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=rf"\%sqraid(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=rf"\%sqraid(?: |$)(.*)" % hl))
async def qraid_event(e):
    await raid_handler(e, QRAID, "QRaid")
