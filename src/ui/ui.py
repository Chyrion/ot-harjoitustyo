from ui.ui_login_view import UILoginView
from ui.ui_user_homeview import UIUserHomeview
from ui.ui_user_newflight import UIUserNewFlight
from ui.ui_user_info import UIUserInfo
from ui.ui_user_newplane import UIUserNewPlane
from datamanager.filemanager import FileManager


class UI:
    def __init__(self, root, users: list, files: FileManager):
        self._root = root
        self._current_view = None
        self._users = users
        self._files = files
        self._selected_user = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = UILoginView(
            self._root, self._users, self._files, self._show_homepage_view)

    def _show_homepage_view(self):
        if self._current_view is not None:
            if isinstance(self._current_view.selected_user, str):
                self._get_selected_user_data(
                    self._current_view.selected_user)
            else:
                self._get_selected_user_data(
                    self._current_view.selected_user.username)
        self._hide_current_view()

        self._current_view = UIUserHomeview(
            self._root, self._selected_user, self._show_new_flight_view, self._show_login_view, self._show_user_info_view)

    def _show_new_flight_view(self):
        self._hide_current_view()

        self._current_view = UIUserNewFlight(
            self._root, self._selected_user, self._files, self._show_homepage_view)

    def _show_user_info_view(self):
        self._hide_current_view()

        self._current_view = UIUserInfo(
            self._root, self._selected_user, self._show_homepage_view, self._show_new_plane_view)

    def _show_new_plane_view(self):
        self._hide_current_view()

        self._current_view = UIUserNewPlane(
            self._root, self._selected_user, self._files, self._show_user_info_view)

    def _get_selected_user_data(self, username: str):
        self._selected_user = self._files.load_user_data_from_file(username)
