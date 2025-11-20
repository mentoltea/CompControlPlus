from . import common
from modules import screen, logger
from modules.commands import command
from tasks import task
import telebot
import PIL.Image

def evaluate_message(message: telebot.types.Message):
    query = message.text
    reply = ""
    
    try:
        t = task.ChainedTask([
            task.BasicTask(command.parse_query_to_blocks, query),
            task.BasicTask(command.evaluate_blocks)
        ])()
        reply = str( task.fetch_unnest(t).get() ) # type: ignore
    except Exception as e:
        reply = str(e)
    
    if not common.bot: return
    common.bot.reply_to(message, reply)
    
    
def evaluate_message_async(message: telebot.types.Message):
    task.ThreadTask(evaluate_message, message)()


def send_screen(img: PIL.Image.Image):
    if not common.bot: return
    try:
        common.bot.send_photo(common.admin, img)
    except Exception as e:
        logger.ERROR(str(e))