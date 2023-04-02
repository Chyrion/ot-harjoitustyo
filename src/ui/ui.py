from ui.ui_login_view import UILoginView
from ui.ui_user_homeview import UIUserHomeview


class UI:
    def __init__(self, root, users, files):
        self._root = root
        self._current_view = None
        self._users = users
        self._files = files

    def start(self):
        self._current_view = UILoginView(
            self._root, self._users, self._files, self._show_homepage_view())

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = UILoginView(
            self._root, self._users, self._files, self._show_homepage_view())

    def _show_homepage_view(self):
        self._hide_current_view()

        self._current_view = UIUserHomeview(self._root, 'Chyrion', self._files)
