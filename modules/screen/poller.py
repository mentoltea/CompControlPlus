from . import screen, state_glue
from core import state
import PIL.Image
from tasks import task
from typing import Callable
import time
from . import common

def poller_function(tid: int, polltime: float, callback: Callable[ [PIL.Image.Image], None] | None = None):
    state_glue.EnsureState()
    countdown = 0
    while True:
        SS = state_glue.GetLocalState()
        
        status = SS.get_status(tid)
        
        if (status == common.STOP):
            SS.set_stopped(tid)
            return
        
        if (countdown <= 0):
            shot = screen.take_screenshot()
            if (callback): callback(shot)
            countdown = polltime
            continue
        
        countdown -= common.DT
        time.sleep(common.DT)


def start_polling(polltime: float, callback: Callable[ [PIL.Image.Image], None] | None = None):
    SS = state_glue.GetLocalState()
    tid = SS.new_tid()
    task.ThreadTask(poller_function, tid, polltime, callback)()