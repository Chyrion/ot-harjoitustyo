from ui.ui_login_view import UILoginView


class UI:
    def __init__(self, root, users):
        self._root = root
        self._current_view = None
        self._users = users

    def start(self):
        self._current_view = UILoginView(self._root, self._users)
