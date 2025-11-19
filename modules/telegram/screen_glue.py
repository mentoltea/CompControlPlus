from . import common
from modules import screen, logger

def send_screen(img: screen.screen.PIL.Image.Image):
    if not common.bot: return
    try:
        common.bot.send_photo(common.admin, img)
    except Exception as e:
        logger.ERROR(str(e))