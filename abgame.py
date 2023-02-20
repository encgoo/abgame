from GameBoard import GameBoard


class AbGame:

    def __init__(self):
        self.gb = GameBoard()

    def run(self):
        self.gb.updater = self
        self.gb.init()
        self.gb.start()

    #
    # This is the method being called for each iteration to update the location of the flying
    # needle.
    def update(self, data):
        # TODO:
        #   This is a linear update for both x and y. You need to do the calculation yourself
        #   You have the speed of the needle gb.data.v_x and gb.data.v_y
        #
        data.n_x += 1
        data.n_y -= 1
        return

    # This is the method to start up a new game. You need to set the location of the virus
    def start_new_game(self):
        # TODO: create a random place for the virus. Make sure it is WITHIN the window
        #   note that the window is from 0 to gb.data.win_w
        self.gb.data.vir_x = 520
        return



if __name__ == '__main__':
    abgame = AbGame()
    abgame.run()
