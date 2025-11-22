from core.functional.utility import ensure_dir_existance
import time

COMMON_DIR = "data/logs/"
FORMAT = ".txt"
BYDIRECT_LOGS_TO_STDOUT = False

def format_filename(t: time.struct_time) -> str:
    return time.strftime("%B %Y", t)

def format_line(t: time.struct_time, text: str) -> str:
    return time.strftime("Day %d %H:%M:%S: ", t) + text + "\n"

def plain_text(text: str):
    ensure_dir_existance(COMMON_DIR)
    current = time.localtime()

    filename = format_filename(current)
    filepath = COMMON_DIR + filename + FORMAT
    
    textline = text
    
    fd = open(filepath, mode="a", encoding="utf-8")
    fd.write(textline)
    fd.close()
    
    if (BYDIRECT_LOGS_TO_STDOUT): print(textline)

def LOG(text: str):
    ensure_dir_existance(COMMON_DIR)
    current = time.localtime()

    filename = format_filename(current)
    filepath = COMMON_DIR + filename + FORMAT
    
    textline = "LOG  : " + format_line(current, text)
    
    fd = open(filepath, mode="a", encoding="utf-8")
    fd.write(textline)
    fd.close()
    
    if (BYDIRECT_LOGS_TO_STDOUT): print(textline)

def INFO(text: str):
    ensure_dir_existance(COMMON_DIR)
    current = time.localtime()

    filename = format_filename(current)
    filepath = COMMON_DIR + filename + FORMAT
    
    textline = "INFO : " + format_line(current, text)
    
    fd = open(filepath, mode="a", encoding="utf-8")
    fd.write(textline)
    fd.close()
    
    if (BYDIRECT_LOGS_TO_STDOUT): print(textline)


def WARN(text: str):
    ensure_dir_existance(COMMON_DIR)
    current = time.localtime()

    filename = format_filename(current)
    filepath = COMMON_DIR + filename + FORMAT
    
    textline = "WARN : " + format_line(current, text)
    
    fd = open(filepath, mode="a", encoding="utf-8")
    fd.write(textline)
    fd.close()
    
    if (BYDIRECT_LOGS_TO_STDOUT): print(textline)

    
def ERROR(text: str):
    ensure_dir_existance(COMMON_DIR)
    current = time.localtime()

    filename = format_filename(current)
    filepath = COMMON_DIR + filename + FORMAT
    
    textline = "ERROR: " + format_line(current, text)
    
    fd = open(filepath, mode="a", encoding="utf-8")
    fd.write(textline)
    fd.close()
    
    if (BYDIRECT_LOGS_TO_STDOUT): print(textline)

    