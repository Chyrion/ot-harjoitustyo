from tkinter import ttk, constants
from datamanager.filemanager import FileManager
from entities.user import User


class UIUserInfo:

    def __init__(self, root, user: User, handle_show_homepage):
        self._root = root
        self._frame = None
        self._user = user

        self._handle_show_homepage = handle_show_homepage

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    @property
    def selected_user(self):
        return self._user.username

    def _initialize(self):
        print(self._user)
        self._frame = ttk.Frame(master=self._root)
        title_label = ttk.Label(self._frame, text='User info', font=(
            'Arial', 16)).grid(row=0, column=0, columnspan=2)

        back_button = ttk.Button(
            self._frame, text='Return', command=self._handle_show_homepage).grid(row=0, column=2)

        name_label = ttk.Label(self._frame, text=self._user.username, font=(
            'Arial', 14)).grid(row=1, column=0, columnspan=2)
        flights_text = ttk.Label(
            self._frame, text='Flights:').grid(row=2, column=0)
        flights_number = ttk.Label(self._frame, text=len(
            self._user.flights)).grid(row=2, column=1)

        self.pack()
