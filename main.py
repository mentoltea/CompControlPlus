from core import state
from modules import screen, logger
from modules import telegram
from modules.commands import command
import global_settings

from tasks import task
import time
import sys

in_background = False
if 'pythonw' in sys.executable:
    in_background = True

logger.plain_text("\n\n")

starttext = "CompControl+ started " + time.asctime()
if in_background: starttext += " in background"
else: starttext += " in foreground"

starttext.replace('\n', '')
logger.LOG(starttext)

telegram.poller.start_polling_async()
time.sleep(2)


if telegram.common.bot:
    telegram.common.bot.send_message(telegram.common.admin, starttext)


afterload = global_settings.MAIN_AFTERLOAD_SCRIPT

if afterload:
    af_text = f"Loading afterload script {afterload}"
    logger.LOG(af_text)
    
    with open(afterload, "r") as f:
        lines = f.readlines()
    for line in lines:
        logger.plain_text("\t" + line + "\n")
        if (line != ""):
            if line[0] != '/' and line[0] != '!': line = '/' + line
            try:
                t = task.ChainedTask([
                    task.BasicTask(command.parse_query_to_blocks, line),
                    task.BasicTask(command.evaluate_blocks)
                ])()
                task.fetch_unnest(t).get() # type: ignore
            except Exception as e:
                logger.ERROR(str(e))
                if (telegram.common.bot): 
                    telegram.common.bot.send_message(telegram.common.admin, str(e))
            

text = ""
while True:
    if (in_background):
        time.sleep(1)
    else: 
        text = input('> ')
        
    if (text != ""):
        logger.INFO(f"Local message: {text}")
        if text[0] != '/' and text[0] != '!': text = '/' + text
        reply = ""
        try:
            t = task.ChainedTask([
                task.BasicTask(command.parse_query_to_blocks, text),
                task.BasicTask(command.evaluate_blocks)
            ])()
            reply = str( task.fetch_unnest(t).get() ) # type: ignore
        except Exception as e:
            logger.ERROR(str(e))
            reply = str(e)
        print(reply)