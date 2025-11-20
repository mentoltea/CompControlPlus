import telebot
from . import common
from typing import Callable, Any

queue: list[ tuple [Callable[..., bool], tuple] ] = []

def empty_queue():
    remove = []
    for (func, args) in queue:
        if not func(*args, noqueue=True): break
        remove.append( (func,args) )
    
    for r in remove:
        queue.remove(r)

def send_message(chat_id: int, text: str, noqueue=False) -> bool:
    try:
        if not common.bot: raise Exception("")
        common.bot.send_message(chat_id, text)
        return True
    except Exception as e:
        if not noqueue: queue.append( (send_message, (chat_id, text)) )
    return False
        

def send_photo(chat_id: int, image, noqueue=False) -> bool:
    try:
        if not common.bot: raise Exception("")
        common.bot.send_photo(chat_id, image)
        return True
    except Exception as e:
        pass
    return False
    
def reply_to(message: telebot.types.Message, text: str, noqueue=False) -> bool:
    try:
        if not common.bot: raise Exception("")
        common.bot.reply_to(message, text)
        return True
    except Exception as e:
        if not noqueue: queue.append( (reply_to, (message, text)) )
    return False