from time import sleep
import rtmidi
from curses import wrapper, curs_set

class AbletonTransport(object):
    def __init__(self): 
        self.midiout = rtmidi.MidiOut()
        self.midiout.open_virtual_port("Ableton Terminal Transport")

    def do(self, key):
        if key == 'p':
            self.midiout.send_message([0xb0, 85, 127])
            return 'Play'
        elif key == 's':
            self.midiout.send_message([0xb0, 86, 127])
            return 'Stop'
        else:
            return 'Press p or s, or q to quit'

    def close(self):
        self.midiout.close_port()



def main(stdscr):
    cli = AbletonTransport()
    stdscr.clear()
    stdscr.refresh()
    curs_set(0)

    key = None
    while not key == 'q':
        key = stdscr.getkey().lower()
        res = cli.do(key)

        stdscr.deleteln()
        stdscr.addstr(0, 0, res)
    cli.close()

if __name__ == '__main__':
    wrapper(main)
