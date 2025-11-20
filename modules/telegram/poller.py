from . import common, send, persistent
import requests
import telebot
import time
from core.functional import program
from modules import logger
from tasks import task

def poll():
    base_wait = 10
    inscrease_wait = 20
    maxiterations = 10
    iterations = 1
    while common.KEEP_POLLING:
        if not common.bot: return
        
        text = f"--- Iteration {iterations} ---"
        logger.LOG(text)
        if (iterations != 1):
            try: send.send_message(common.admin, text)
            except Exception as e: logger.ERROR(str(e))
        
        try:
            common.bot.polling(non_stop=True)
        except requests.exceptions.ConnectionError as e:
            logger.ERROR(str(e))
        except telebot.apihelper.ApiException as e:
            logger.ERROR(str(e))
        except Exception as e:
            logger.ERROR(str(e))
            
        iterations += 1
        if (iterations > maxiterations):
            persistent.keep_trying_to_start_async()
            return
            # logger.WARN("Too many iterations, rebooting...")
            # program.reboot()
        
        time.sleep(base_wait + inscrease_wait*(iterations-1))

def start_polling():
    common.KEEP_POLLING = True
    poll()

def start_polling_async():
    task.ThreadTask(start_polling)()
    
def stop_polling():
    if not common.bot: return
    common.KEEP_POLLING = False
    
    common.bot.stop_polling()
    common.bot.stop_bot()
    time.sleep(10)

    common.bot = None