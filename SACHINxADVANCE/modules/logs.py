import asyncio
import heroku3
from pymongo import MongoClient
from config import SACHIN0, SACHIN1, SACHIN2, SACHIN3, SACHIN4, SACHIN5, SACHIN6, SACHIN7, SACHIN8, SACHIN9, MONGO_DB_URI, SUDO_USERS, OWNER_ID, HEROKU_API_KEY, HEROKU_APP_NAME, CMD_HNDLR as hl
from datetime import datetime
from telethon import events
from telethon.errors import ForbiddenError
from telethon.tl.custom import Button

# MongoDB configuration
client = MongoClient(MONGO_DB_URI)
db = client['bot_database']
stats_collection = db['stats']

# Heroku logs URL
AYU = "https://graph.org/file/3a93e14b4e1c6c1d031e7.mp4"

async def fetch_heroku_logs(ANNIE):
    if HEROKU_APP_NAME is None or HEROKU_API_KEY is None:
        await ANNIE.reply("First set these vars in Heroku: `HEROKU_API_KEY` and `HEROKU_APP_NAME`.")
        return None

    try:
        heroku_conn = heroku3.from_key(HEROKU_API_KEY)
        app = heroku_conn.app(HEROKU_APP_NAME)
    except Exception:
        await ANNIE.reply("Make sure your Heroku API Key and App Name are configured correctly in Heroku.")
        return None

    return app.get_log()

async def write_logs_to_file(logs):
    with open("SACHINxADVANCElogs.txt", "w") as logfile:
        logfile.write("𖤍 ᴊᴀʀᴠɪs 𖤍 [ ʙᴏᴛ ʟᴏɢs ]\n\n" + logs)

async def send_logs_file(ANNIE, ms):
    try:
        await X1.send_file(ANNIE.chat_id, "SACHINxADVANCElogs.txt", caption=f"𝗝𝗔𝗥𝗩𝗜𝗦 𝗕𝗢𝗧𝗦 𝗟𝗢𝗚𝗦 📨\n\n  » **Time Taken:** `{ms} seconds`")
    except Exception as e:
        await ANNIE.reply(f"An Exception Occurred!\n\n**ERROR:** {str(e)}")

@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
async def logs(ANNIE):
    if ANNIE.sender_id == OWNER_ID:
        start = datetime.now()
        fetch = await ANNIE.reply("__Fetching Logs...__")
        logs = await fetch_heroku_logs(ANNIE)

        if logs is not None:
            await write_logs_to_file(logs)
            end = datetime.now()
            ms = (end - start).seconds
            await asyncio.sleep(1)
            await send_logs_file(ANNIE, ms)
            await fetch.delete()
    elif ANNIE.sender_id in SUDO_USERS:
        await ANNIE.reply("**»** ᴏɴʟʏ ᴊᴀʀᴠɪs ᴄᴀɴ ᴘᴇʀғᴏʀᴍ ᴛʜɪs ᴀᴄᴛɪᴏɴ...")

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
async def track_stats(event):
    if event.is_group:
        group_id = event.chat_id
        stats_collection.update_one(
            {'type': 'group', 'id': group_id},
            {'$set': {'id': group_id}},
            upsert=True
        )
    elif event.is_private:
        user_id = event.sender_id
        stats_collection.update_one(
            {'type': 'user', 'id': user_id},
            {'$set': {'id': user_id}},
            upsert=True
        )

@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
async def check_stats(event):
    if event.sender_id == OWNER_ID or event.sender_id in SUDO_USERS:
        user_count = stats_collection.count_documents({'type': 'user'})
        group_count = stats_collection.count_documents({'type': 'group'})
        stats_message = f"⚔️ 𝗝𝗔𝗥𝗩𝗜𝗦 𝗦𝗢𝗟𝗢 𝗦𝗧𝗔𝗧𝗦 ⚔️"
        
        await event.reply(stats_message, file=AYU, buttons=[
            [Button.inline("ᴜsᴇʀs", data="user_stats"), Button.inline("ᴄʜᴀᴛs", data="group_stats")],
            [Button.inline("ᴏᴠᴇʀᴀʟʟ", data="overall_stats")]
        ])
    else:
        await event.reply("ʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴍᴇɴᴜ.")

@SACHIN0.on(events.CallbackQuery)
@SACHIN1.on(events.CallbackQuery)
@SACHIN2.on(events.CallbackQuery)
@SACHIN3.on(events.CallbackQuery)
@SACHIN4.on(events.CallbackQuery)
@SACHIN5.on(events.CallbackQuery)
@SACHIN6.on(events.CallbackQuery)
@SACHIN7.on(events.CallbackQuery)
@SACHIN8.on(events.CallbackQuery)
@SACHIN9.on(events.CallbackQuery)
async def callback(event):
    data = event.data.decode('utf-8')
    if data == "user_stats":
        user_count = stats_collection.count_documents({'type': 'user'})
        buttons = [[Button.inline("ʙᴀᴄᴋ", data="back_to_stats")]]
        await event.edit(f"ᴛᴏᴛᴀʟ ᴜsᴇʀs: {user_count}", buttons=buttons)
    elif data == "group_stats":
        group_count = stats_collection.count_documents({'type': 'group'})
        buttons = [[Button.inline("ʙᴀᴄᴋ", data="back_to_stats")]]
        await event.edit(f"ᴄʜᴀᴛs: {group_count}", buttons=buttons)
    elif data == "overall_stats":
        user_count = stats_collection.count_documents({'type': 'user'})
        group_count = stats_collection.count_documents({'type': 'group'})
        buttons = [[Button.inline("ʙᴀᴄᴋ", data="back_to_stats")]]
        await event.edit(f"ᴛᴏᴛᴀʟ ᴜsᴇʀs: {user_count}\nᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs: {group_count}", buttons=buttons)
    elif data == "back_to_stats":
        buttons = [
            [Button.inline("ᴜsᴇʀs", data="user_stats"), Button.inline("ᴄʜᴀᴛs", data="group_stats")],
            [Button.inline("ᴏᴠᴇʀᴀʟʟ", data="overall_stats")]
        ]
        await event.edit("⚔️ 𝗝𝗔𝗥𝗩𝗜𝗦 𝗦𝗢𝗟𝗢 𝗦𝗧𝗔𝗧𝗦 ⚔️", file=AYU, buttons=buttons)

@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
async def broadcast(event):
    if event.sender_id == OWNER_ID:
        reply = await event.get_reply_message()
        message = event.pattern_match.group(1)

        if not message and not reply:
            await event.reply("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ.")
            return
        
        users = stats_collection.find({'type': 'user'})
        groups = stats_collection.find({'type': 'group'})

        user_count = 0
        group_count = 0

        for user in users:
            try:
                if reply:
                    await X1.send_message(user['id'], message or reply.text, file=reply.media)
                else:
                    await X1.send_message(user['id'], message)
                user_count += 1
            except ForbiddenError:
                pass  # Ignore if the bot is blocked
            except Exception as e:
                print(f"Error sending message to {user['id']}: {str(e)}")
        
        for group in groups:
            try:
                if reply:
                    await X1.send_message(group['id'], message or reply.text, file=reply.media)
                else:
                    await X1.send_message(group['id'], message)
                group_count += 1
            except ForbiddenError:
                pass  # Ignore if the bot is removed from the group
            except Exception as e:
                print(f"Error sending message to {group['id']}: {str(e)}")
        
        await event.reply(f"ʙʀᴏᴀᴅᴄᴀsᴛ ʜᴀs ʙᴇᴇɴ ᴄᴏᴍᴘʟᴇᴛᴇᴅ.\n\nᴍᴇssᴀɢᴇ sᴇɴᴛ ᴛᴏ {user_count} ᴜsᴇʀs ᴀɴᴅ {group_count} ɢʀᴏᴜᴘs.")
    else:
        await event.reply("ᴏɴʟʏ ᴊᴀʀᴠɪs ᴄᴀɴ ᴘᴇʀғᴏʀᴍ ᴛʜɪs ᴀᴄᴛɪᴏɴ.")
