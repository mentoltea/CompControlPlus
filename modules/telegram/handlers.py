import telebot
from . import common, glue

from modules import logger
import time

def text_handler(message: telebot.types.Message):
    if not common.bot: return
    if message.date < time.time() - common.MAX_TIME_SHIFT: return
    
    
    logstr = "Message "
    if message.chat.id != common.admin:
        logstr += f"from {str(message.chat.first_name)} {str(message.chat.last_name)} ({str(message.chat.id)})"
        logstr += " : " + str(message.text)
        logger.INFO(logstr)
        return
    
    if not message.text: return
    
    logstr += " : " + str(message.text)
    logger.INFO(logstr)
    if message.text[0] != '/' and message.text[0] != '!': message.text = '/' + message.text
    
    glue.evaluate_message_async(message)
    

def photo_handler(message: telebot.types.Message):
    if not common.bot: return
    if message.chat.id != common.admin: return
    if message.date < time.time() - common.MAX_TIME_SHIFT: return


def document_handler(message: telebot.types.Message):
    if not common.bot: return
    if message.chat.id != common.admin: return
    if message.date < time.time() - common.MAX_TIME_SHIFT: return