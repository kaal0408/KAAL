from telethon import events, buttons

from System import ALIVE_NAME
from System.utils import admin_cmd, sudo_cmd
from System.Config import Config, Var

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "kααl uѕєr"

@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def omkvai(event):
  omk_caption = f"**{CUSTOM_ALIVE}**\n\n"
  omk_caption += f"**kααl вσt íѕ αlívє**\n\n"
  omk_caption += "αвσut mч ѕчѕtєm ✗\n\n"
  omk_caption += f"**kααl uѕєr** ☞ [{DEFAULTUSER}](tg://user?id={fuk})\n"
  omk_caption += f"**kααl ᴠᴇʀ**: `{lionver}`\n"
  omk_caption += f"**tєlєthσn vєrѕíσn** ☞ {version.__version__}\n"
  omk_caption += f"**kααl ѕuppσrt grσup** ☞ [ᴊᴏɪɴ](https://t.me/Murat_30_God)\n"
  omk_caption += f"**lícєnѕє**  ☞ [𝚃𝙴𝙰𝙼 𝚉𝚈𝙿𝙷𝙴𝚁](https://github.com/kaal0408/KAAL)\n"
  omk_caption += (
        f"**©️ cσpчríght вч** ☞ [𝚉𝚈𝙿𝙷𝙴𝚁 𝚇](https://github.com/kaal0408/KAAL)\n\n"
    )
  omk_button = [[Button.url("kααl uѕєr", f"https://t.me/{bot.me.username}")]]
  omk_button += [[Button.url("kααl ѕuppσrt grσup", "t.me/Murat_30_God"), Button.url("кααℓ υρ∂αтεs", "t.me/Murat_30_God")]]
  omk_button += [[custom.Button.inline("dєplσч kααl uѕєrвσt", data="omkd")]]
  await tgbot.send_file(event.chat_id, captions=omk_caption) 

  
