from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ɪɴᴄʟᴜᴅᴇ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✬ ᴄᴏᴍᴍᴀɴᴅѕ ✬", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="⚡ ᴛʜᴄ ѕʜᴀʏᴀʀɪ 💫", url=f"https://t.me/THC_SHAYRI_CHANNEL"
            )
        ],
        [
            InlineKeyboardButton(
                text="✬ sᴜᴩᴩᴏʀᴛ ✬", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="✬ ᴄʀᴇᴀᴛᴏʀ ✬", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="✬ ꜱʜᴀʏᴀʀɪ ✬", url=f"https://t.me/TootaShayaR"
            ),
            InlineKeyboardButton(
                text="💬 ᴛʜᴄ ᴄʜᴀᴛ ✬", url=f"https://t.me/+1dITv_e9l0ZhNzVl"
            )
        ],
     ]
    return buttons
