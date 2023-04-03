from tkinter import ttk, constants
from datamanager.filemanager import FileManager


class UILoginView:
    """Login view for the user"""

    def __init__(self, root, users: list, files: FileManager, handle_user_select):
        """Class constructor"""

        self._root = root
        self._frame = None
        self._users = users
        self._files = files
        self._user_labels = []
        self._new_user_field = None
        self._handle_user_select = handle_user_select
        self._selected_user = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        main_label = ttk.Label(master=self._frame, text='Select user')
        main_label.grid(row=0, column=0, sticky=constants.E)
        self._initialize_user_list()

        self._new_user_field = ttk.Entry(master=self._frame)
        self._new_user_field.grid(padx=5, pady=5)
        new_user_button = ttk.Button(
            master=self._frame, text='Create new user', command=self._new_user)
        new_user_button.grid(padx=5, pady=5)

        self.pack()

    def select_user(self, user):
        self._selected_user = user
        self._handle_user_select()

    def _initialize_user_list(self):
        """Creates a label + button for each user in the user list"""

        for user in self._users:
            label = ttk.Label(master=self._frame, text=user)
            button = ttk.Button(master=self._frame, text='Select',
                                command=lambda: self.select_user(user))
            self._user_labels.append((label, button))

        for i in range(len(self._user_labels)):
            self._user_labels[i][0].grid(padx=5, pady=5)
            self._user_labels[i][1].grid(padx=5, pady=5)

    def _new_user(self):
        if len(self._new_user_field.get()) > 3:
            print('Trying to save new user')
            new_user_name = self._new_user_field.get()
            self._files.new_user(new_user_name)

    def selected_user(self):
        return self._selected_user
