from conway import Conway
from time import sleep
from background import *

if __name__ == '__main__':
    c = Conway(51, 126)
    while True:
        if not c.has_alive_cell or not c.has_changed:
            c.initGrid()
        c.run()
        changeBackground(c.__str__())
        sleep(0.05)