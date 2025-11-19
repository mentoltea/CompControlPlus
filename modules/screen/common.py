import time

DT = 1

WORKING = 0
STOP = 1
STOPPED = 2

COMMON_DIR = "data/screenshots/"

class ScreenState():
    def __init__(self):
        self.counter: int = 0
        self.poller_tids: dict[int, int] = {}
    
    def new_tid(self) -> int:
        tid = self.counter
        self.counter += 1
        self.poller_tids[tid] = WORKING
        return tid
    
    def set_stop(self, tid):
        self.poller_tids[tid] = STOP
        
    def set_stopped(self, tid):
        self.poller_tids[tid] = STOPPED
        
    def get_status(self, tid):
        return self.poller_tids[tid]
    
    def __del__(self):
        for tid in self.poller_tids:
            self.poller_tids[tid] = STOP
        # ensure all threads got stop signal
        time.sleep(DT*2)