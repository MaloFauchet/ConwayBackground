from PIL import Image, ImageDraw
from time import perf_counter
import ctypes
import sys


def process_str(string):
    return string.replace("n", "\n")

def createNewImage(grid: str) -> None:
    img = Image.new('RGB', (1920, 1080), color='black')
    d = ImageDraw.Draw(img)
    d.multiline_text((10, 10), grid, fill=(255, 255, 255), spacing=10)
    img.save('background.png')


def changeBackground(grid: str) -> None:
    new_str = process_str(grid)
    createNewImage(new_str)
    ctypes.windll.user32.SystemParametersInfoW(0x14, 0, f"{sys.path[0]}\\background.png", 0x2)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("ERROR : TOO MUCH ARGUMENTS ", sys.argv)
        exit(1)

    changeBackground(sys.argv[1])
