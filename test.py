import regular_task
import time
import inspect
from typing import Any


def func(a: int|None, b, c="123", d=None, **kwargs):
    print(time.time())
    
sign = inspect.signature(func)
for param in sign.parameters.values():
    print(f"Parameter: {param.name}")
    print(f"\tType: {param.annotation}")