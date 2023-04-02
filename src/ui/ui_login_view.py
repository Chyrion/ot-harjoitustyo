from tkinter import ttk, constants


class UILoginView:
    """Login view for the user"""

    def __init__(self, root, users):
        """Class constructor"""

        self._root = root
        self._frame = None
        self._users = users
        self._user_labels = []

        self._initalize()

    def destroy(self):
        self._frame.destroy()

    def _initalize(self):
        self._frame = ttk.Frame(master=self._root)
        main_label = ttk.Label(master=self._root, text='Select user')
        main_label.grid(row=0, column=0, sticky=constants.E)
        self._initialize_user_list()

    def _initialize_user_list(self):
        self._frame = ttk.Frame(master=self._root)
        for user in self._users:
            label = ttk.Label(master=self._root, text=user)
            button = ttk.Button(master=self._root, text='Select')
            self._user_labels.append((label, button))
        for i in range(len(self._user_labels)):
            self._user_labels[i][0].grid(row=i+1, column=0)
            self._user_labels[i][1].grid(row=i+1, column=1)
