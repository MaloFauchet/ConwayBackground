from conway import Conway
from time import sleep

if __name__ == '__main__':
    c = Conway()
    while c.has_alive_cell and c.has_changed:
        c.run()
        print("\n\n\n\n\n\n")
        print(c)
        sleep(1)