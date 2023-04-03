from tkinter import ttk
from datamanager.filemanager import FileManager


class UIUserHomeview:
    """Responsible for creating the home page for a user"""

    def __init__(self, root, username: str, files: FileManager):
        self._root = root
        self._frame = None
        self._username = username
        self._files = files

        self._userdata = self._load_data()

        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        name_label = ttk.Label(
            master=self._root, text=self._userdata['username'])
        name_label.grid(row=0, column=0)

    def _load_data(self):
        return self._files.load_user_data(self._username)
