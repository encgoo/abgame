from GameBoard import GameBoard

class AbGame:

    def __init__(self):
        self.gb = GameBoard(False)

    def run(self):
        self.gb.updater = self
        self.gb.init()

        # set virus pos
        self.gb.data.vir_x = self.gb.data.w / 2
        # set needle pos
        self.gb.data.n_x = self.gb.data.w / 2
        self.gb.data.n_y = self.gb.data.ground_y - 100
        self.gb.set_flying()

        self.gb.start()

    def update(self, data):
        return

if __name__ == '__main__':
    abgame = AbGame()
    abgame.run()
