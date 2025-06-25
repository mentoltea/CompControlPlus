from tasks import task
import time

class RegularTask(task.ThreadTask):
    """
    Calls target regularly over given interval in seconds.
    """
    
    def __init__(
        self,
        target: task.Callable,
        interval: float,
        *args, **kwargs               
    ):
        self.stopflag: bool = False
        self.interval = interval
          
        def task_wrapper(*args, **kwargs):               
            while (not self.stopflag):
                self.result_ = target(*args, **kwargs)
                time.sleep(self.interval)

        super().__init__(task_wrapper, *args, **kwargs)
    
    def stop(self):
        self.stopflag = True