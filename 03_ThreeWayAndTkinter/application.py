from game_process import GameProcess
from game_view import GameView


class Application:
    _TITLE = 'CrazyGameDev'
    _WINDOW_SIZE = '500x500'
    _RANG = 4

    def __init__(self):
        print('Application init')
        self._game_process = GameProcess(
            rang=self._RANG,
        )
        self._game_view = GameView(
            title=self._TITLE,
            window_size=self._WINDOW_SIZE,
            game_process=self._game_process,
        )
