from random import shuffle

from common import ButtonMeta
from common import Coords

import consts


class GameProcess:
    def __init__(self, rang,):
        print('GameProcess init')
        self._rang = rang
        self.buttons = {}
        self.arrange_buttons()

    def arrange_buttons(self):
        rang = self._rang
        ids = list(range(rang * rang))
        shuffle(ids)
        ids = (x for x in ids)
        for row in range(rang):
            for column in range(rang):
                id = next(ids)
                self.buttons[id] = ButtonMeta(
                    Coords(row, column),
                    handler=lambda id=id: self._button_click(id)
                )

    def _button_click(self, id):
        print(f'>>>>>>> btn {id} clicked')
        empty_btn = self.buttons[consts.EMPTY_BUTTON_ID]
        cur_btn = self.buttons[id]
        tmp_empty_btn_coords = empty_btn.coords
        empty_btn.coords = cur_btn.coords
        cur_btn.coords = tmp_empty_btn_coords
