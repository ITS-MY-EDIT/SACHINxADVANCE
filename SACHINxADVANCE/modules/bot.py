## Copy Paster Must Give Credit...
## @JARVIS_V2

import sys
import heroku3
from os import execl, getenv
from datetime import datetime
from telethon import events, Button
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from config import SACHIN0, SACHIN1, SACHIN2, SACHIN3, SACHIN4, SACHIN5, SACHIN6, SACHIN7, SACHIN8, SACHIN9, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl

REQUIRED_CHANNELS = ["JARVIS_V_SUPPORT", "Dora_Hub"]


@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(event):
    if event.sender_id in SUDO_USERS:
        start = datetime.now()
        reply_message = await event.reply("❄️")
        end = datetime.now()
        ping_time = (end - start).microseconds / 1000
        await reply_message.edit(f"[𝐉𝐀𝐑𝐕𝐈𝐒 𝐈𝐒 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐇𝐀𝐓𝐄𝐑𝐒 🥀](https://t.me/JARVIS_V_SUPPORT)🤖\n» `{ping_time} ᴍꜱ`")
    else:
        await prompt_join_channels(event)











@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))

async def restart(event):
    if event.sender_id in SUDO_USERS:
        await event.reply("`ʙᴏᴛ ɪs ʀᴇsᴛᴀʀᴛɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ`")
        try:
            await X1.disconnect()
        except Exception:
            pass
        execl(sys.executable, sys.executable, *sys.argv)
    else:
        await prompt_join_channels(event)









@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        await manage_sudo_users(event, add=True)
    elif event.sender_id in SUDO_USERS:
        await event.reply("ᴏɴʟʏ ᴊᴀʀᴠɪs ᴄᴀɴ ᴀᴅᴅ sᴜᴅᴏ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ʙʏ .ɢᴇᴛsᴜᴅᴏ")
    else:
        await prompt_join_channels(event)
        
        
        
        
        
        
        
        

@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
async def removesudo(event):
    if event.sender_id == OWNER_ID:
        await manage_sudo_users(event, add=False)
    else:
        await event.reply("ᴏɴʟʏ ᴊᴀʀᴠɪs ᴄᴀɴ ʀᴇᴍᴏᴠᴇ sᴜᴅᴏ ᴜsᴇʀs")








@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))

async def show_sudo_users(event):
    if event.sender_id == OWNER_ID:
        sudo_users_list = "sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ:\n" + "\n".join(f"- {user_id}" for user_id in SUDO_USERS)
        await event.reply(sudo_users_list)
    else:
        await event.reply("ᴛʜɪs ғᴜɴᴄᴛɪᴏɴ ᴄᴀɴ ᴏɴʟʏ ᴘᴇʀғᴏʀᴍ ʙʏ ᴊᴀʀᴠɪs")








@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%saddmultisudo(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%saddmultisudo(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%saddmultisudo(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%saddmultisudo(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%saddmultisudo(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%saddmultisudo(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%saddmultisudo(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%saddmultisudo(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%saddmultisudo(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%saddmultisudo(?: |$)(.*)" % hl))

async def addmultisudo(event):
    if event.sender_id == OWNER_ID:
        await manage_multiple_sudo_users(event)
    elif event.sender_id in SUDO_USERS:
        await event.reply("ᴏɴʟʏ ᴊᴀʀᴠɪs ᴄᴀɴ ᴀᴅᴅ ᴍᴜʟᴛɪsᴜᴅᴏ ᴜsᴇʀs ᴀᴛ ᴀ ᴛɪᴍᴇ.")
    else:
        await prompt_join_channels(event)







@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))

async def getsudo(event):
    if event.sender_id not in SUDO_USERS:
        for channel in REQUIRED_CHANNELS:
            try:
                participants = await X1(GetParticipantsRequest(
                    channel=channel,
                    filter=ChannelParticipantsSearch(''),
                    offset=0,
                    limit=100,
                    hash=0
                ))
                if not any(participant.id == event.sender_id for participant in participants.users):
                    await prompt_join_channels(event)
                    return
            except Exception as ex:
                await event.reply(f"ᴇʀʀᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇᴍʙᴇʀsʜɪᴘ ғᴏʀ {channel}: {ex}")
                return
        await manage_sudo_users(event, add=True)
    else:
        await event.reply("ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ ʜᴀᴠᴇ sᴜᴅᴏ ᴘʀɪᴠɪʟʟᴇɢᴇs")







@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
async def verify(event):
    if await verify_membership(event):
        await manage_sudo_users(event, add=True)
        await event.reply("ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴠᴇʀɪғɪᴇᴅ ᴀɴᴅ ᴀᴜᴛʜᴏʀɪsᴇᴅ ғᴏʀ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ")
    else:
        await prompt_join_channels(event)

async def manage_sudo_users(event, add):
    heroku = heroku3.from_key(HEROKU_API_KEY)
    sudousers = getenv("SUDO_USERS", default="")
    target = str(event.sender_id)

    if HEROKU_APP_NAME:
        app = heroku.app(HEROKU_APP_NAME)
    else:
        await event.reply("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
        return

    heroku_var = app.config()
    if add:
        if target in sudousers.split():
            await event.reply("ᴛʜɪs ɢᴜʏ ɪs ᴀʟʀᴇᴀᴅʏ ɪɴ ᴛʜᴇ sᴜᴅᴏ ᴜsᴇʀ ʟɪsᴛ.")
        else:
            new_sudo_users = f"{sudousers} {target}".strip()
            heroku_var["SUDO_USERS"] = new_sudo_users
            await event.reply(f"ᴀᴅᴅᴇᴅ ɴᴇᴡ sᴜᴅᴏ ᴜsᴇʀs: `{target}`. ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ.")
    else:
        if target not in sudousers.split():
            await event.reply("ᴜsᴇʀ ɪɴ ɴᴏᴛ ɪs sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ.")
        else:
            new_sudo_users = " ".join(user for user in sudousers.split() if user != target)
            heroku_var["SUDO_USERS"] = new_sudo_users
            await event.reply(f"ʀᴇᴍᴏᴠɪɴɢ ᴀʟʟ sᴜᴅᴏ ᴘᴏᴡᴇʀs: `{target}`")

async def manage_multiple_sudo_users(event):
    heroku = heroku3.from_key(HEROKU_API_KEY)
    sudousers = getenv("SUDO_USERS", default="")
    if HEROKU_APP_NAME:
        app = heroku.app(HEROKU_APP_NAME)
    else:
        await event.reply("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
        return

    heroku_var = app.config()
    try:
        target_ids = [str(int(x)) for x in event.pattern_match.group(1).split()]
    except ValueError:
        await event.reply("Error processing the user IDs.")
        return

    new_sudo_users = set(sudousers.split())
    new_sudo_users.update(target_ids)
    heroku_var["SUDO_USERS"] = " ".join(new_sudo_users)
    await event.reply(f"ᴀᴅᴅᴇᴅ {len(target_ids)} ɴᴇᴡ sᴜᴅᴏ ᴜsᴇʀs ɪɴ ᴛʜᴇ ʟɪsᴛ.")

async def prompt_join_channels(event):
    buttons = [
        [Button.url("ᴊᴀʀᴠɪs sᴜᴘᴘᴏʀᴛ", "https://t.me/JARVIS_V_SUPPORT")],
        [Button.url("sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", "https://t.me/Dora_Hub")],
        [Button.inline("ᴠᴇʀɪғʏ ✅", b"verify_membership")]
    ]
    await event.reply("ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ, ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴠᴀʀs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪғʏ:", buttons=buttons)








@SACHIN0.on(events.CallbackQuery(data=b"verify_membership"))
@SACHIN1.on(events.CallbackQuery(data=b"verify_membership"))
@SACHIN2.on(events.CallbackQuery(data=b"verify_membership"))
@SACHIN3.on(events.CallbackQuery(data=b"verify_membership"))
@SACHIN4.on(events.CallbackQuery(data=b"verify_membership"))
@SACHIN5.on(events.CallbackQuery(data=b"verify_membership"))
@SACHIN6.on(events.CallbackQuery(data=b"verify_membership"))
@SACHIN7.on(events.CallbackQuery(data=b"verify_membership"))
@SACHIN8.on(events.CallbackQuery(data=b"verify_membership"))
@SACHIN9.on(events.CallbackQuery(data=b"verify_membership"))
async def verify_membership(event):
    if await verify_membership(event):
        await manage_sudo_users(event, add=True)
        await event.reply("ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴠᴇʀɪғɪᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ✅\nᴀᴅᴅᴇᴅʏᴏᴜ ɪɴ sᴜᴅᴏ ᴜsᴇʀs!")
    else:
        await prompt_join_channels(event)

async def verify_membership(event):
    for channel in REQUIRED_CHANNELS:
        try:
            participants = await X1(GetParticipantsRequest(
                channel=channel,
                filter=ChannelParticipantsSearch(''),
                offset=0,
                limit=100,
                hash=0
            ))
            if not any(participant.id == event.sender_id for participant in participants.users):
                return False
        except Exception as ex:
            await event.reply(f"Error checking membership for {channel}: {ex}")
            return False
    return True
