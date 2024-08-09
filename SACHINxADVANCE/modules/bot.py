import sys
import heroku3
from os import execl, getenv
from datetime import datetime
from telethon import events, Button
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from config import SACHIN0, SACHIN1, SACHIN2, SACHIN3, SACHIN4, SACHIN5, SACHIN6, SACHIN7, SACHIN8, SACHIN9, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl

REQUIRED_CHANNELS = ["ALL_SANATANI_BOT", "I_M_FIGHTER"]


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
        await reply_message.edit(f"**┬─ ⋅ ⋅ ───── ᯽ ───── ⋅ ⋅ ─┬**\n**      ❖│sᴧɴᴧᴛᴧηɪ ꭙ sᴘᴧϻ│❖**\n**┼─ ⋅ ⋅ ───── ᯽ ───── ⋅ ⋅ ─┴**\n**│˹❄️˼ ᴘɪηɢ ᴘσηɢ :** `{ping_time} ϻs`\n**├──────────────────**\n**│˹⛈️˼ ʟᴧsᴛ ᴜᴘᴅᴧᴛᴇ :** `12:06:24`\n**├──────────────────**\n**│˹⚡˼ ʟɪᴠᴇ sᴛᴧᴛᴜs : ɪ ᴧᴍ ᴧʟɪᴠᴇ**\n**└──────────────────**")
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
        await event.reply("**┬─ ⋅ ⋅ ───── ᯽ ───── ⋅ ⋅ ─┬**\n**      ❖│sᴧɴᴧᴛᴧηɪ ꭙ sᴘᴧϻ│❖**\n**┼─ ⋅ ⋅ ───── ᯽ ───── ⋅ ⋅ ─┴**\n**│˹🍃˼ ʀᴇʙᴏᴏᴛ ᴘʀᴏᴄᴇss sᴛᴀʀᴛ**\n**├──────────────────**\n**│˹🍀˼ ɪ'ᴍ ʙᴀᴄᴋ ɪɴ ᴛᴡᴏ ᴍɪɴᴜᴛᴇs**\n**├──────────────────**\n**│˹⚡˼ ʟɪᴠᴇ sᴛᴧᴛᴜs : ɪ ᴧᴍ ᴧʟɪᴠᴇ**\n**└──────────────────**")
        try:
            await SACHIN0.disconnect()
        except Exception:
            pass
        try:
            await SACHIN1.disconnect()
        except Exception:
            pass
        try:
            await SACHIN2.disconnect()
        except Exception:
            pass
        try:
            await SACHIN3.disconnect()
        except Exception:
            pass
        try:
            await SACHIN4.disconnect()
        except Exception:
            pass
        try:
            await SACHIN5.disconnect()
        except Exception:
            pass
        try:
            await SACHIN6.disconnect()
        except Exception:
            pass
        try:
            await SACHIN7.disconnect()
        except Exception:
            pass
        try:
            await SACHIN8.disconnect()
        except Exception:
            pass
        try:
            await SACHIN9.disconnect()
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
        await event.reply("ᴏɴʟʏ sᴀᴄʜɪɴ ᴄᴀɴ ᴀᴅᴅ sᴜᴅᴏ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ʙʏ .ɢᴇᴛsᴜᴅᴏ")
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
        await event.reply("ᴏɴʟʏ sᴀᴄʜɪɴ ᴄᴀɴ ʀᴇᴍᴏᴠᴇ sᴜᴅᴏ ᴜsᴇʀs")








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
        await event.reply("ᴛʜɪs ғᴜɴᴄᴛɪᴏɴ ᴄᴀɴ ᴏɴʟʏ ᴘᴇʀғᴏʀᴍ ʙʏ sᴀᴄʜɪɴ")








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
        await event.reply("ᴏɴʟʏ sᴀᴄʜɪɴ sᴀɴᴀᴛᴀɴɪ ᴄᴀɴ ᴀᴅᴅ ᴍᴜʟᴛɪsᴜᴅᴏ ᴜsᴇʀs ᴀᴛ ᴀ ᴛɪᴍᴇ.")
    else:
        await prompt_join_channels(event)



#----------------------------------------------------------------------------------------------------------------------------------------------------

@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
async def getsudo(event):
    if event.sender_id not in SUDO_USERS:
        for channel in REQUIRED_CHANNELS:
            try:
                participants = await SACHIN0(GetParticipantsRequest(
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

@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
async def getsudo(event):
    if event.sender_id not in SUDO_USERS:
        for channel in REQUIRED_CHANNELS:
            try:
                participants = await SACHIN1(GetParticipantsRequest(
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
        
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
async def getsudo(event):
    if event.sender_id not in SUDO_USERS:
        for channel in REQUIRED_CHANNELS:
            try:
                participants = await SACHIN2(GetParticipantsRequest(
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

@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
async def getsudo(event):
    if event.sender_id not in SUDO_USERS:
        for channel in REQUIRED_CHANNELS:
            try:
                participants = await SACHIN3(GetParticipantsRequest(
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
        
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
async def getsudo(event):
    if event.sender_id not in SUDO_USERS:
        for channel in REQUIRED_CHANNELS:
            try:
                participants = await SACHIN4(GetParticipantsRequest(
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

@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
async def getsudo(event):
    if event.sender_id not in SUDO_USERS:
        for channel in REQUIRED_CHANNELS:
            try:
                participants = await SACHIN5(GetParticipantsRequest(
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

@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
async def getsudo(event):
    if event.sender_id not in SUDO_USERS:
        for channel in REQUIRED_CHANNELS:
            try:
                participants = await SACHIN6(GetParticipantsRequest(
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
        
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
async def getsudo(event):
    if event.sender_id not in SUDO_USERS:
        for channel in REQUIRED_CHANNELS:
            try:
                participants = await SACHIN7(GetParticipantsRequest(
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
        
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
async def getsudo(event):
    if event.sender_id not in SUDO_USERS:
        for channel in REQUIRED_CHANNELS:
            try:
                participants = await SACHIN8(GetParticipantsRequest(
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
        
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
async def getsudo(event):
    if event.sender_id not in SUDO_USERS:
        for channel in REQUIRED_CHANNELS:
            try:
                participants = await SACHIN9(GetParticipantsRequest(
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
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#----------------------------------------------------------------------------------------------------------------------------------------------------
        












@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
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
        [Button.url("❖ | sᴀɴᴀᴛᴀɴɪ ꭙ ʙᴏᴛ | ❖", "https://t.me/ALL_SANATANI_BOT")],
        [Button.url("❖ | 4ˢᵗ ꭙ ғɪɢʜᴛᴇʀ | ❖", "https://t.me/i_m_fighter")],
        [Button.inline("❖ | ᴠᴇʀɪғʏ | ❖", b"verify_membership")]
    ]
    await event.reply("ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ, ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴠᴀʀs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪғʏ:", buttons=buttons)


@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
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
        [Button.url("❖ | sᴀɴᴀᴛᴀɴɪ ꭙ ʙᴏᴛ | ❖", "https://t.me/ALL_SANATANI_BOT")],
        [Button.url("❖ | 4ˢᵗ ꭙ ғɪɢʜᴛᴇʀ | ❖", "https://t.me/i_m_fighter")],
        [Button.inline("❖ | ᴠᴇʀɪғʏ | ❖", b"verify_membership")]
    ]
    await event.reply("ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ, ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴠᴀʀs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪғʏ:", buttons=buttons)


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
        [Button.url("❖ | sᴀɴᴀᴛᴀɴɪ ꭙ ʙᴏᴛ | ❖", "https://t.me/ALL_SANATANI_BOT")],
        [Button.url("❖ | 4ˢᵗ ꭙ ғɪɢʜᴛᴇʀ | ❖", "https://t.me/i_m_fighter")],
        [Button.inline("❖ | ᴠᴇʀɪғʏ | ❖", b"verify_membership")]
    ]
    await event.reply("ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ, ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴠᴀʀs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪғʏ:", buttons=buttons)

    

@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
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
        [Button.url("❖ | sᴀɴᴀᴛᴀɴɪ ꭙ ʙᴏᴛ | ❖", "https://t.me/ALL_SANATANI_BOT")],
        [Button.url("❖ | 4ˢᵗ ꭙ ғɪɢʜᴛᴇʀ | ❖", "https://t.me/i_m_fighter")],
        [Button.inline("❖ | ᴠᴇʀɪғʏ | ❖", b"verify_membership")]
    ]
    await event.reply("ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ, ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴠᴀʀs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪғʏ:", buttons=buttons)

    
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
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
        [Button.url("❖ | sᴀɴᴀᴛᴀɴɪ ꭙ ʙᴏᴛ | ❖", "https://t.me/ALL_SANATANI_BOT")],
        [Button.url("❖ | 4ˢᵗ ꭙ ғɪɢʜᴛᴇʀ | ❖", "https://t.me/i_m_fighter")],
        [Button.inline("❖ | ᴠᴇʀɪғʏ | ❖", b"verify_membership")]
    ]
    await event.reply("ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ, ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴠᴀʀs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪғʏ:", buttons=buttons)

    

@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
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
        [Button.url("❖ | sᴀɴᴀᴛᴀɴɪ ꭙ ʙᴏᴛ | ❖", "https://t.me/ALL_SANATANI_BOT")],
        [Button.url("❖ | 4ˢᵗ ꭙ ғɪɢʜᴛᴇʀ | ❖", "https://t.me/i_m_fighter")],
        [Button.inline("❖ | ᴠᴇʀɪғʏ | ❖", b"verify_membership")]
    ]
    await event.reply("ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ, ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴠᴀʀs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪғʏ:", buttons=buttons)

    

@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
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
        [Button.url("❖ | sᴀɴᴀᴛᴀɴɪ ꭙ ʙᴏᴛ | ❖", "https://t.me/ALL_SANATANI_BOT")],
        [Button.url("❖ | 4ˢᵗ ꭙ ғɪɢʜᴛᴇʀ | ❖", "https://t.me/i_m_fighter")],
        [Button.inline("❖ | ᴠᴇʀɪғʏ | ❖", b"verify_membership")]
    ]
    await event.reply("ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ, ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴠᴀʀs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪғʏ:", buttons=buttons)

    

@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
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
        [Button.url("❖ | sᴀɴᴀᴛᴀɴɪ ꭙ ʙᴏᴛ | ❖", "https://t.me/ALL_SANATANI_BOT")],
        [Button.url("❖ | 4ˢᵗ ꭙ ғɪɢʜᴛᴇʀ | ❖", "https://t.me/i_m_fighter")],
        [Button.inline("❖ | ᴠᴇʀɪғʏ | ❖", b"verify_membership")]
    ]
    await event.reply("ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ, ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴠᴀʀs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪғʏ:", buttons=buttons)

    
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
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
        [Button.url("❖ | sᴀɴᴀᴛᴀɴɪ ꭙ ʙᴏᴛ | ❖", "https://t.me/ALL_SANATANI_BOT")],
        [Button.url("❖ | 4ˢᵗ ꭙ ғɪɢʜᴛᴇʀ | ❖", "https://t.me/i_m_fighter")],
        [Button.inline("❖ | ᴠᴇʀɪғʏ | ❖", b"verify_membership")]
    ]
    await event.reply("ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ, ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴠᴀʀs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪғʏ:", buttons=buttons)

    
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
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
        [Button.url("❖ | sᴀɴᴀᴛᴀɴɪ ꭙ ʙᴏᴛ | ❖", "https://t.me/ALL_SANATANI_BOT")],
        [Button.url("❖ | 4ˢᵗ ꭙ ғɪɢʜᴛᴇʀ | ❖", "https://t.me/i_m_fighter")],
        [Button.inline("❖ | ᴠᴇʀɪғʏ | ❖", b"verify_membership")]
    ]
    await event.reply("ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ, ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴠᴀʀs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪғʏ:", buttons=buttons)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
#----------------------------------------------------------------------------------------------------------------------------------------------------
















@SACHIN0.on(events.CallbackQuery(data=b"verify_membership"))
async def verify_membership(event):
    if await verify_membership(event):
        await manage_sudo_users(event, add=True)
        await event.reply("ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴠᴇʀɪғɪᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ✅\nᴀᴅᴅᴇᴅʏᴏᴜ ɪɴ sᴜᴅᴏ ᴜsᴇʀs!")
    else:
        await prompt_join_channels(event)

async def verify_membership(event):
    for channel in REQUIRED_CHANNELS:
        try:
            participants = await SACHIN0(GetParticipantsRequest(
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
    
    
@SACHIN1.on(events.CallbackQuery(data=b"verify_membership"))
async def verify_membership(event):
    if await verify_membership(event):
        await manage_sudo_users(event, add=True)
        await event.reply("ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴠᴇʀɪғɪᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ✅\nᴀᴅᴅᴇᴅʏᴏᴜ ɪɴ sᴜᴅᴏ ᴜsᴇʀs!")
    else:
        await prompt_join_channels(event)

async def verify_membership(event):
    for channel in REQUIRED_CHANNELS:
        try:
            participants = await SACHIN1(GetParticipantsRequest(
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
    
    
@SACHIN2.on(events.CallbackQuery(data=b"verify_membership"))
async def verify_membership(event):
    if await verify_membership(event):
        await manage_sudo_users(event, add=True)
        await event.reply("ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴠᴇʀɪғɪᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ✅\nᴀᴅᴅᴇᴅʏᴏᴜ ɪɴ sᴜᴅᴏ ᴜsᴇʀs!")
    else:
        await prompt_join_channels(event)

async def verify_membership(event):
    for channel in REQUIRED_CHANNELS:
        try:
            participants = await SACHIN2(GetParticipantsRequest(
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
    
    
@SACHIN3.on(events.CallbackQuery(data=b"verify_membership"))
async def verify_membership(event):
    if await verify_membership(event):
        await manage_sudo_users(event, add=True)
        await event.reply("ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴠᴇʀɪғɪᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ✅\nᴀᴅᴅᴇᴅʏᴏᴜ ɪɴ sᴜᴅᴏ ᴜsᴇʀs!")
    else:
        await prompt_join_channels(event)

async def verify_membership(event):
    for channel in REQUIRED_CHANNELS:
        try:
            participants = await SACHIN3(GetParticipantsRequest(
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
    
    
@SACHIN4.on(events.CallbackQuery(data=b"verify_membership"))
async def verify_membership(event):
    if await verify_membership(event):
        await manage_sudo_users(event, add=True)
        await event.reply("ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴠᴇʀɪғɪᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ✅\nᴀᴅᴅᴇᴅʏᴏᴜ ɪɴ sᴜᴅᴏ ᴜsᴇʀs!")
    else:
        await prompt_join_channels(event)

async def verify_membership(event):
    for channel in REQUIRED_CHANNELS:
        try:
            participants = await SACHIN4(GetParticipantsRequest(
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
    
    
@SACHIN5.on(events.CallbackQuery(data=b"verify_membership"))
async def verify_membership(event):
    if await verify_membership(event):
        await manage_sudo_users(event, add=True)
        await event.reply("ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴠᴇʀɪғɪᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ✅\nᴀᴅᴅᴇᴅʏᴏᴜ ɪɴ sᴜᴅᴏ ᴜsᴇʀs!")
    else:
        await prompt_join_channels(event)

async def verify_membership(event):
    for channel in REQUIRED_CHANNELS:
        try:
            participants = await SACHIN5(GetParticipantsRequest(
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
    
    
@SACHIN6.on(events.CallbackQuery(data=b"verify_membership"))
async def verify_membership(event):
    if await verify_membership(event):
        await manage_sudo_users(event, add=True)
        await event.reply("ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴠᴇʀɪғɪᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ✅\nᴀᴅᴅᴇᴅʏᴏᴜ ɪɴ sᴜᴅᴏ ᴜsᴇʀs!")
    else:
        await prompt_join_channels(event)

async def verify_membership(event):
    for channel in REQUIRED_CHANNELS:
        try:
            participants = await SACHIN6(GetParticipantsRequest(
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
    
    
@SACHIN7.on(events.CallbackQuery(data=b"verify_membership"))
async def verify_membership(event):
    if await verify_membership(event):
        await manage_sudo_users(event, add=True)
        await event.reply("ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴠᴇʀɪғɪᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ✅\nᴀᴅᴅᴇᴅʏᴏᴜ ɪɴ sᴜᴅᴏ ᴜsᴇʀs!")
    else:
        await prompt_join_channels(event)

async def verify_membership(event):
    for channel in REQUIRED_CHANNELS:
        try:
            participants = await SACHIN7(GetParticipantsRequest(
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
    
    
@SACHIN8.on(events.CallbackQuery(data=b"verify_membership"))
async def verify_membership(event):
    if await verify_membership(event):
        await manage_sudo_users(event, add=True)
        await event.reply("ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴠᴇʀɪғɪᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ✅\nᴀᴅᴅᴇᴅʏᴏᴜ ɪɴ sᴜᴅᴏ ᴜsᴇʀs!")
    else:
        await prompt_join_channels(event)

async def verify_membership(event):
    for channel in REQUIRED_CHANNELS:
        try:
            participants = await SACHIN8(GetParticipantsRequest(
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
            participants = await SACHIN9(GetParticipantsRequest(
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
    
    
