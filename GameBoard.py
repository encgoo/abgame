from GameBoardMocked import GameBoardMocked
from GameBoardReal import GameBoardReal
from Data import Data

class GameBoard:

    def __init__(self, mocked=False):
        self.win_w = 800
        self.win_h = 600

        self.bg_color = (255, 255, 255)
        self.fps = 60

        self.title = 'Powered by GameBoard'

        self.updater = None
        self.data = None

        if mocked:
            self.gb = GameBoardMocked(self)
        else:
            self.gb = GameBoardReal(self)

    def init(self):
        # separate this from __init__ so caller can
        # have a change to change the params
        self.data = Data(self.win_w, self.win_h)
        self.gb.init()

    def start(self):
        self.gb.start()


if __name__ == '__main__':
    gb = GameBoard(False)
    gb.init()
    gb.start()

