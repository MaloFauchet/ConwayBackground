from conway import Conway
from time import sleep, perf_counter
from background import *

if __name__ == '__main__':
    c = Conway(51, 126)
    while True:
        if not c.has_alive_cell or not c.has_changed:
            c.initGrid()

        c.run()

        with open("tmp.txt", 'w') as f:
            f.write(c.__str__())
        changeBackground(c.__str__())
        sleep(0.05)