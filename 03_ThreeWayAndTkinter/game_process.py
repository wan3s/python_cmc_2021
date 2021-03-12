from random import shuffle

from common import ButtonMeta
from common import Coords

import consts


class GameProcess:
    def __init__(self, rang,):
        print('GameProcess init')
        self._rang = rang
        self.arrange_buttons()

    def arrange_buttons(self):
        self.buttons = {}
        rang = self._rang
        ids = list(range(rang * rang))
        shuffle(ids)
        print(f'^^^^^^^^^^^^^^^^ {ids}')
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
        if (
            abs(empty_btn.coords.row - cur_btn.coords.row) +
            abs(empty_btn.coords.column - cur_btn.coords.column)
        ) > 1:
            return
        tmp_empty_btn_coords = empty_btn.coords
        empty_btn.coords = cur_btn.coords
        cur_btn.coords = tmp_empty_btn_coords

        self._check_finish()

    def _check_finish(self):
        for i in range(self._rang * self._rang):
            if i == consts.EMPTY_BUTTON_ID:
                continue

            cur_row = self.buttons[i].coords.row
            cur_column = self.buttons[i].coords.column

            if (
                cur_row != (i - 1) // self._rang or
                cur_column != (i - 1) % self._rang
            ):
                return
            print('You win')

