from game_view import GameView

class Application:
    _TITLE = 'CrazyGameDev'
    _WINDOW_SIZE = '500x500'

    def __init__(self):
        self._game_view = GameView(self._TITLE, self._WINDOW_SIZE)