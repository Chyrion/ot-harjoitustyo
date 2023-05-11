from tkinter import ttk, constants
from datamanager.filemanager import FileManager


class UILoginView:
    """Login view for the user"""

    def __init__(self, root, users: list, files: FileManager, handle_user_select):
        """Class constructor

        args:
            root:
                TKinter object that the view is contained in
            users:
                List of all users
            files:
                FileManager which is responsible for handling file operations
            handle_user_select:
                Method which is responsible for handling user selection
        """

        self._root = root
        self._frame = None
        self._users = users
        self._files = files
        self._user_labels = []
        self._new_user_field = None
        self._new_user_button = None
        self._handle_user_select = handle_user_select
        self._selected_user = None
        self._row = 1

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        main_label = ttk.Label(master=self._frame, text='Select user')
        main_label.grid(columnspan=2)

        for user in self._users:
            self._initialize_user(user)

        self._initalize_new_user_field()

        self.pack()

    def select_user(self, user):
        self._selected_user = user
        self._handle_user_select()

    def _initialize_user(self, user):
        """Creates a label + button for each user in the user list"""

        label = ttk.Label(master=self._frame, text=user)
        button = ttk.Button(master=self._frame, text='Select',
                            command=lambda: self.select_user(user))
        self._user_labels.append((label, button))

        label.grid(column=0, row=self._row, padx=2, pady=2)
        button.grid(column=1, row=self._row, padx=2, pady=2)
        self._row += 1

    def _initalize_new_user_field(self):
        if self._new_user_field:
            self._new_user_field.destroy()
        if self._new_user_button:
            self._new_user_button.destroy()

        self._new_user_field = ttk.Entry(master=self._frame)
        self._new_user_field.grid(
            column=0, row=self._row, padx=5, pady=5, sticky=constants.S)
        self._new_user_button = ttk.Button(
            master=self._frame, text='Create new user', command=self._new_user)
        self._new_user_button.grid(
            column=1, row=self._row, padx=5, pady=5, sticky=constants.S)

    def _new_user(self):
        if len(self._new_user_field.get()) > 3:
            print('Trying to save new user')
            new_user_name = self._new_user_field.get()
            add = self._files.new_user(new_user_name)
            self._initialize_user(new_user_name)
            self._initalize_new_user_field()

    @property
    def selected_user(self):
        return self._selected_user
