
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.errors import capture_err
import httpx

start_txt = """**
✪ ωεℓ¢σмє ƒσя Rᴏʟᴇx ʙᴀʙʏ яєρσѕ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""

@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
            InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/baby_music_bot?startgroup=true")
        ],
        [
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/DEMON_BOT_SUPPORT"),
            InlineKeyboardButton("ᴏᴡɴᴇʀ ʀᴏʟᴇx", url="https://t.me/ll_ROLEX_lll"),
        ],
        [
            InlineKeyboardButton("ᴄʜᴀᴛ ɢʀᴏᴜᴘ", url="https://t.me/FUKRA_DEMON"),
            InlineKeyboardButton("ᴅᴇᴍᴏɴ ɴᴇᴛᴡᴏʀᴋ", url="http://t.me/DEMON_NETWORKS"),
         
        ],
        [
            InlineKeyboardButton("𝗕𝗔𝗡 𝗔𝗟𝗟︎", url=f"https://github.com/Sunnykumar1122/BABYBANALL"),
            InlineKeyboardButton("︎ʙᴀʙʏ X ᴍᴜsɪᴄ", url=f"https://github.com/Sunnykumar1122/BABYMUSIC"),
        ],
        [
             InlineKeyboardButton("ᴢᴇɴɪɴ X ᴍᴜɪsᴄ", url=f"https://github.com/Sunnykumar1122/zeninXmuisc"), 
              InlineKeyboardButton("ᴄʜᴀᴛ ʙᴏᴛ", url=f"https://github.com/Sunnykumar1122/misschatbot"),
            
        ],
        [   
             InlineKeyboardButton("sᴘᴀᴍ ʙᴏᴛ", url=f"https://github.com/Sunnykumar1122/ROLEX_SPAM"),
            InlineKeyboardButton("︎ᴜsᴇʀ ʙᴏᴛ", url=f"https://github.com/Sunnykumar1122/BABYUSER")
    ],
     
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await msg.reply_photo(
        photo="https://telegra.ph//file/a9e8e650ac5b49d504902.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )

@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/DAXXTEAM/DAXXMUSIC/contributors")
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1
        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/Sunnyjumar1122/BABYMUSIC) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/FUKRA_DEMON)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
