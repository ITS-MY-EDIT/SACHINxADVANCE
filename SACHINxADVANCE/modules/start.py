## Copy Paster Must Give Credit...
## @JARVIS_V2

from telethon import __version__, events, Button
from config import SACHIN0, SACHIN1, SACHIN2, SACHIN3, SACHIN4, SACHIN5, SACHIN6, SACHIN7, SACHIN8, SACHIN9

# Constants
START_BUTTON = [
    [
        Button.url("🍁 sᴀᴄʜɪɴ", "https://t.me/V_VIP_OWNER"),
        Button.url("ᴜsᴇʀʙᴏᴛ 🕸️", "https://t.me/SANATANI_X_ROBOT")
    ],
    [
        Button.inline("🥀 ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs 🥀", data="help_back")
    ],
    [
        Button.url("✨ ᴜᴘᴅᴀᴛᴇ", "https://t.me/All_SANATANI_BOT"),
        Button.url("sᴜᴘᴘᴏʀᴛ ❄️", "https://t.me/+Ckzm2ypQyIIzZTll")
    ],
    [
        Button.url("🌸 ᴊᴏɪɴ ғᴏʀ sᴜᴅᴏ 🌸", "https://t.me/+Ckzm2ypQyIIzZTll")
    ],
]

IMAGE_URL = "https://telegra.ph//file/7cfeff721589b61a2f634.jpg"

async def get_bot_info(event):
    ANNIE = await event.client.get_me()
    bot_name = ANNIE.first_name
    bot_id = ANNIE.id
    return bot_name, bot_id

def create_start_text(bot_name, bot_id, sender_name, sender_id):
    return (
        f"**╭────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ⏤͟͟͞͞‌‌‌‌★**\n"
        f"**┆**\n"
        f"**┊◍ ʜᴇʏ : [{sender_name}](tg://user?id={sender_id}) **\n"
        f"**┆◍ ɪ ᴀᴍ : [{bot_name}](tg://user?id={bot_id}) **\n"
        f"**┊**\n"
        f"**┆● sᴀɴᴀᴛᴀɴɪ ʙᴏᴛ ᴠᴇʀsɪᴏɴ :** `0.2`\n"
        f"**┊● ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `8.2.5.1.01`\n"
        f"**╰─────────────────────────**\n"
        f"**──────────────────────────**\n"
        f"**⦿ Oᴡɴᴇʀ - [🦋⃟‌🇸ʌᷟᴄᷣʜɪ֟፝η 🌸](https://t.me/v_vip_owner) | [🦋⃟‌🇸ʌᷟᴄᷣʜɪ֟፝η 🌸](https://t.me/sachin_owner) **\n"
        f"**──────────────────────────**\n"
        f"**    ❖ Uᴘᴅᴀᴛᴇ's ⏤͟͟͞͞‌‌‌‌ [❖ ∣ Sᴀɴᴀᴛᴀɴɪ Tᴇᴄʜ ∣ ❖](https://t.me/all_sanatani_bot) **\n"
         "**──────────────────────────**"
    )

@SACHIN0.on(events.NewMessage(pattern="/start"))
@SACHIN1.on(events.NewMessage(pattern="/start"))
@SACHIN2.on(events.NewMessage(pattern="/start"))
@SACHIN3.on(events.NewMessage(pattern="/start"))
@SACHIN4.on(events.NewMessage(pattern="/start"))
@SACHIN5.on(events.NewMessage(pattern="/start"))
@SACHIN6.on(events.NewMessage(pattern="/start"))
@SACHIN7.on(events.NewMessage(pattern="/start"))
@SACHIN8.on(events.NewMessage(pattern="/start"))
@SACHIN9.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        bot_name, bot_id = await get_bot_info(event)
        start_text = create_start_text(bot_name, bot_id, event.sender.first_name, event.sender.id)
        await event.client.send_file(
            event.chat_id,
            IMAGE_URL,
            caption=start_text,
            buttons=START_BUTTON
        )
