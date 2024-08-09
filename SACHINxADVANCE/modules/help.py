## Copy Paster Must Give Credit...
## @JARVIS_V2

from telethon import events, Button
from config import SACHIN0, SACHIN1, SACHIN2, SACHIN3, SACHIN4, SACHIN5, SACHIN6, SACHIN7, SACHIN8, SACHIN9, SUDO_USERS, CMD_HNDLR as hl

HELP_STRING = (
    "**•┬── ⋅ ⋅ ─────᯽───── ⋅ ⋅ ──┬•**\n"
    "** ❖ sʌηʌᴛʌηɪ֟፝ sᴘʌᴍ ʙᴏᴛ ʜʟᴘ ᴍᴇηꭎ֟፝᷍ ❖**\n"
    "**•┴── ⋅ ⋅ ─────᯽───── ⋅ ⋅ ──┴•**\n"
    "**•────•❅•°σᴡηᴇʀ ɪ֟፝ηғσ°•❅•────•**\n"
    "**•┬───────────────────┬•**\n"
    "**       ❖ ∣ [s ʌᷟ ᴄᷣ ʜ ɪ֟፝ η](https://t.me/v_vip_owner) | [s ʌᷟ ᴄᷣ ʜ ɪ֟፝ η](https://t.me/sachin_owner) ∣ ❖ **\n"
    "**•┴───────────────────┴•**\n"
    "**•┬───•❅•°ʙσᴛ ꭎ֟፝᷍ᴘᴅʌᴛᴇs°•❅•───┬•**\n"
    "**•┬───────────────────┬•**\n"
    "**             [❖ ∣ Sᴀɴᴀᴛᴀɴɪ Tᴇᴄʜ ∣ ❖](https://t.me/All_SANATANI_BOT) **\n"
    "**•┴───────────────────┴•**\n"
)

HELP_BUTTONS = [
    [Button.inline("• ꜱᴘᴀᴍ •", data="spam"), Button.inline("• ʀᴀɪᴅ •", data="raid")],
    [Button.inline("• ᴇxᴛʀᴀ •", data="extra")],
    [Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/All_SANATANI_BOT"),
     Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/+eXx77DN2rstkMWQ1")]
]

EXTRA_MSG = (
    f"**» ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ:**\n\n"
    f"𝗢𝗪𝗡𝗘𝗥: **ᴏᴡɴᴇʀ ᴄᴍᴅꜱ**\n"
    f"  1) {hl}ping\n"
    f"  2) {hl}reboot\n"
    f"  3) {hl}broadcast\n"
    f"  4) {hl}stats\n"
    f"  5) {hl}sudo <reply to user>\n"
    f"  6) {hl}logs ➪ Owner Cmd\n"
    f"𝗘𝗖𝗛𝗢: **ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ**\n"
    f"  1) {hl}echo <reply to user>\n"
    f"  2) {hl}rmecho <reply to user>\n\n"
    f"𝗟𝗘𝗔𝗩𝗘: **ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ**\n"
    f"  1) {hl}leave <group/chat id>\n"
    f"  2) {hl}leave : ᴛʏᴘᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ\n\n"
    f"**@V_VIP_OWNER**"
)

RAID_MSG = (
    f"**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ:**\n\n"
    f"𝗥𝗔𝗜𝗗: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜꜱᴇʀ ꜰᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ.**\n"
    f"  1) {hl}raid <count> <username>\n"
    f"  2) {hl}raid <count> <reply to user>\n\n"
    f"𝗥𝗘𝗣𝗟𝗬 𝗥𝗔𝗜𝗗: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**\n"
    f"  1) {hl}rraid <replying to user>\n"
    f"  2) {hl}rraid <username>\n\n"
    f"𝗗𝗥𝗘𝗣𝗟𝗬 𝗥𝗔𝗜𝗗: **ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**\n"
    f"  1) {hl}drraid <replying to user>\n"
    f"  2) {hl}drraid <username>\n\n"
    f"𝗠-𝗥𝗔𝗜𝗗:  **ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**\n"
    f"  1) {hl}mraid <count> <username>\n"
    f"  2) {hl}mraid <count> <reply to user>\n\n"
    f"𝗦-𝗥𝗔𝗜𝗗: **ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**\n"
    f"  1) {hl}sraid <count> <username>\n"
    f"  2) {hl}sraid <count> <reply to user>\n\n"
    f"𝗤-𝗥𝗔𝗜𝗗: **ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**\n"
    f"  1) {hl}qraid <count> <username>\n"
    f"  2) {hl}qraid <count> <reply to user>\n\n"
    f"**© @V_VIP_OWNER**"
)

SPAM_MSG = (
    f"**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:**\n\n"
    f"𝗦𝗣𝗔𝗠: **ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ.**\n"
    f"  1) {hl}spam <count> <message to spam>\n"
    f"  2) {hl}spam <count> <replying any message>\n\n"
    f"𝗣𝗥𝗢𝗡-𝗦𝗣𝗔𝗠: **ᴘᴏʀɴᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ.**\n"
    f"  1) {hl}pspam <count>\n\n"
    f"𝗛𝗔𝗡𝗚: **ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇꜱ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ.**\n"
    f"  1) {hl}hang <counter>\n\n"
    f"**© @V_VIP_OWNER**"
)

def is_sudo_user(user_id):
    return user_id in SUDO_USERS

async def send_help_message(event):
    await event.client.send_file(
        event.chat_id,
        "https://telegra.ph/file/b6cfab255fabdaabaa89c.jpg",
        caption=HELP_STRING,
        buttons=HELP_BUTTONS
    )

async def send_error_message(event, error):
    await event.client.send_message(event.chat_id, f"An Exception Occured!\n\n**ERROR:** {str(error)}")

async def handle_help_back(event):
    await event.edit(
        HELP_STRING,
        buttons=HELP_BUTTONS
    )

async def handle_callback_query(event, message, back_button_data):
    await event.edit(
        message,
        buttons=[[Button.inline("< Back", data=back_button_data)],]
    )

async def handle_callback_query_error(event):
    await event.answer(".ᴘɪɴɢ ᴛʏᴘᴇ ᴋᴀʀ ᴋᴇ ᴄʜᴀɴɴᴇʟ ᴊᴏɪɴ ᴋᴀʀᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄ sᴜᴅᴏ ᴍɪʟ ᴊᴀʏᴇɢᴀ", cache_time=0, alert=True)

@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if is_sudo_user(event.sender_id):
        try:
            await send_help_message(event)
        except Exception as e:
            await send_error_message(event, e)

@SACHIN0.on(events.CallbackQuery(pattern=r"help_back"))
@SACHIN1.on(events.CallbackQuery(pattern=r"help_back"))
@SACHIN2.on(events.CallbackQuery(pattern=r"help_back"))
@SACHIN3.on(events.CallbackQuery(pattern=r"help_back"))
@SACHIN4.on(events.CallbackQuery(pattern=r"help_back"))
@SACHIN5.on(events.CallbackQuery(pattern=r"help_back"))
@SACHIN6.on(events.CallbackQuery(pattern=r"help_back"))
@SACHIN7.on(events.CallbackQuery(pattern=r"help_back"))
@SACHIN8.on(events.CallbackQuery(pattern=r"help_back"))
@SACHIN9.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if is_sudo_user(event.query.user_id):
        await handle_help_back(event)
    else:
        await handle_callback_query_error(event)

@SACHIN0.on(events.CallbackQuery(pattern=r"spam"))
@SACHIN1.on(events.CallbackQuery(pattern=r"spam"))
@SACHIN2.on(events.CallbackQuery(pattern=r"spam"))
@SACHIN3.on(events.CallbackQuery(pattern=r"spam"))
@SACHIN4.on(events.CallbackQuery(pattern=r"spam"))
@SACHIN5.on(events.CallbackQuery(pattern=r"spam"))
@SACHIN6.on(events.CallbackQuery(pattern=r"spam"))
@SACHIN7.on(events.CallbackQuery(pattern=r"spam"))
@SACHIN8.on(events.CallbackQuery(pattern=r"spam"))
@SACHIN9.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if is_sudo_user(event.query.user_id):
        await handle_callback_query(event, SPAM_MSG, "help_back")
    else:
        await handle_callback_query_error(event)

@SACHIN0.on(events.CallbackQuery(pattern=r"raid"))
@SACHIN1.on(events.CallbackQuery(pattern=r"raid"))
@SACHIN2.on(events.CallbackQuery(pattern=r"raid"))
@SACHIN3.on(events.CallbackQuery(pattern=r"raid"))
@SACHIN4.on(events.CallbackQuery(pattern=r"raid"))
@SACHIN5.on(events.CallbackQuery(pattern=r"raid"))
@SACHIN6.on(events.CallbackQuery(pattern=r"raid"))
@SACHIN7.on(events.CallbackQuery(pattern=r"raid"))
@SACHIN8.on(events.CallbackQuery(pattern=r"raid"))
@SACHIN9.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if is_sudo_user(event.query.user_id):
        await handle_callback_query(event, RAID_MSG, "help_back")
    else:
        await handle_callback_query_error(event)

@SACHIN0.on(events.CallbackQuery(pattern=r"extra"))
@SACHIN1.on(events.CallbackQuery(pattern=r"extra"))
@SACHIN2.on(events.CallbackQuery(pattern=r"extra"))
@SACHIN3.on(events.CallbackQuery(pattern=r"extra"))
@SACHIN4.on(events.CallbackQuery(pattern=r"extra"))
@SACHIN5.on(events.CallbackQuery(pattern=r"extra"))
@SACHIN6.on(events.CallbackQuery(pattern=r"extra"))
@SACHIN7.on(events.CallbackQuery(pattern=r"extra"))
@SACHIN8.on(events.CallbackQuery(pattern=r"extra"))
@SACHIN9.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if is_sudo_user(event.query.user_id):
        await handle_callback_query(event, EXTRA_MSG, "help_back")
    else:
        await handle_callback_query_error(event)
