from GameBoard import GameBoard

class AbGame:

    def __init__(self):
        self.gb = GameBoard(False)

    def run(self):
        self.gb.updater = self
        self.gb.init()

        self.gb.data.vir_x = self.gb.data.w / 2

        self.gb.start()

    def update(self, data):
        return

if __name__ == '__main__':
    abgame = AbGame()
    abgame.run()
