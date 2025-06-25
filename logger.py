import utility
import time

COMMON_DIR = "logs/"

LOG_DIR = "log/"
INFO_DIR = "info/"
WARN_DIR = "warn/"
ERROR_DIR = "error/"

FORMAT = ".txt"

def format_filename(t: time.struct_time) -> str:
    return time.strftime("%B %Y", t)

def format_line(t: time.struct_time, text: str) -> str:
    return time.strftime("Day %d %H:%M:%S: ", t) + text + "\n"

def LOG(text: str):
    utility.ensure_dir_existance(COMMON_DIR + LOG_DIR)
    current = time.gmtime()

    filename = format_filename(current)
    filepath = COMMON_DIR + LOG_DIR + filename + FORMAT
    
    textline = format_line(current, text)
    
    fd = open(filepath, mode="a", encoding="utf-8")
    fd.write(textline)
    fd.close()

def INFO(text: str):
    utility.ensure_dir_existance(COMMON_DIR + INFO_DIR)
    current = time.gmtime()

    filename = format_filename(current)
    filepath = COMMON_DIR + INFO_DIR + filename + FORMAT
    
    textline = format_line(current, text)
    
    fd = open(filepath, mode="a", encoding="utf-8")
    fd.write(textline)
    fd.close()

def WARN(text: str):
    utility.ensure_dir_existance(COMMON_DIR + WARN_DIR)
    current = time.gmtime()

    filename = format_filename(current)
    filepath = COMMON_DIR + WARN_DIR + filename + FORMAT
    
    textline = format_line(current, text)
    
    fd = open(filepath, mode="a", encoding="utf-8")
    fd.write(textline)
    fd.close()
    
def ERROR(text: str):
    utility.ensure_dir_existance(COMMON_DIR + ERROR_DIR)
    current = time.gmtime()

    filename = format_filename(current)
    filepath = COMMON_DIR + ERROR_DIR + filename + FORMAT
    
    textline = format_line(current, text)
    
    fd = open(filepath, mode="a", encoding="utf-8")
    fd.write(textline)
    fd.close()
    