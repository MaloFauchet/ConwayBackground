from PIL import Image, ImageDraw
import ctypes
import sys

def createNewImage(grid: str) -> None:
    img = Image.new('RGB', (1920, 1080), color='black')
    d = ImageDraw.Draw(img)
    d.multiline_text((10, 10), grid, fill=(255, 255, 255), spacing=10)
    img.save('background.png')

def changeBackground(grid: str) -> None:
    createNewImage(grid)
    ctypes.windll.user32.SystemParametersInfoW(0x14, 0,f"{sys.path[0]}\\background.png", 0x2)
