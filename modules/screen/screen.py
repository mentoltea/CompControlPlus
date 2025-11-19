import time
import PIL
import PIL.Image
import pyautogui
from core.functional import utility
from . import common

"""Note: changes the original image"""
def add_cursor(img: PIL.Image.Image, mouse_pos: pyautogui.Point, size=3) -> None:
    (sizex, sizey) = img.size
    for x in range(mouse_pos.x - size, mouse_pos.x + size): 
        for y in range(mouse_pos.y - size, mouse_pos.y + size):
            if (x < 0 or x >= sizex): continue
            if (y < 0 or y >= sizey): continue
            
            pixel: tuple[int,int,int] = img.getpixel((x,y)) # type: ignore
            img.putpixel((x,y), (255 - pixel[0], 255 - pixel[1], 255 - pixel[2]))

def take_pure_screenshot() -> PIL.Image.Image:
    img = pyautogui.screenshot()
    mouse_pos = pyautogui.position()
    
    add_cursor(img, mouse_pos)
    
    return img


def save_screenshot(img: PIL.Image.Image):
    current = time.gmtime()
    
    # this variant makes dates like "Y2025/M06/D12" instead of "Y2025/M6/D12"
    # dirpath = time.strftime("Y%Y/M%m/D%d/", current)
    dirpath = f"Y{current.tm_year}/M{current.tm_mon}/D{current.tm_mday}/"
    
    utility.ensure_dir_existance(common.COMMON_DIR + dirpath)
    
    filename = time.strftime("%H-%M-%S", current) + ".png"
    
    img.save(common.COMMON_DIR + dirpath + filename)
    

def take_screenshot() -> PIL.Image.Image:
    img = take_pure_screenshot()
    mouse = pyautogui.position()
    add_cursor(img, mouse)
    save_screenshot(img)
    return img