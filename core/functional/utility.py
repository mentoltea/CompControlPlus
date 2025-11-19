import os
import inspect

def ensure_dir_existance(path: str):
    if not os.path.exists(path):
        os.makedirs(path)