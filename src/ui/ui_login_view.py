from tkinter import ttk, constants
from datamanager.filemanager import FileManager
from datamanager.load_user_data import UserDataLoader
from datamanager.save_user_data import UserDataSaver


class UILoginView:
    """Login view for the user"""

    def __init__(self, root, users, files, handle_user_select):
        """Class constructor"""

        self._root = root
        self._frame = None
        self._users = users
        self._files = files
        self._user_labels = []
        self._new_user_field = None
        self._handle_user_select = handle_user_select

        self._initalize()

    def destroy(self):
        self._frame.destroy()

    def _initalize(self):
        self._frame = ttk.Frame(master=self._root)
        main_label = ttk.Label(master=self._root, text='Select user')
        main_label.grid(row=0, column=0, sticky=constants.E)
        self._initialize_user_list()

        self._new_user_field = ttk.Entry(master=self._root)
        self._new_user_field.grid(padx=5, pady=5)
        new_user_button = ttk.Button(
            master=self._root, text='Create new user', command=self._new_user)
        new_user_button.grid(padx=5, pady=5)

    def _initialize_user_list(self):
        for user in self._users:
            label = ttk.Label(master=self._root, text=user)
            button = ttk.Button(master=self._root, text='Select',
                                command=None)
            self._user_labels.append((label, button))
        for i in range(len(self._user_labels)):
            self._user_labels[i][0].grid(row=i+1, column=0)
            self._user_labels[i][1].grid(row=i+1, column=1)

    def _new_user(self):
        if len(self._new_user_field.get()) > 3:
            print('Trying to save new user')
            new_user_name = self._new_user_field.get()
            saver = UserDataSaver(new_user_name)
            saver.save_to_file(self._files)
