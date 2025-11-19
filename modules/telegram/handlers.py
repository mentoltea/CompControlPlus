import telebot
from . import common

from modules.commands import command, basic_commands
from tasks import task

def text_handler(message: telebot.types.Message):
    if not common.bot: return
    if message.chat.id != common.admin: return

    if not message.text: return
    
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
        
    common.bot.reply_to(message, reply)

def photo_handler(message: telebot.types.Message):
    if not common.bot: return
    if message.chat.id != common.admin: return

def document_handler(message: telebot.types.Message):
    if not common.bot: return
    if message.chat.id != common.admin: return
