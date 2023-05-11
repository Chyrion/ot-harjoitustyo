from tkinter import ttk, constants
from datamanager.filemanager import FileManager
from entities.user import User


class UIUserNewPlane:
    '''Responsible for creating a view for adding new planes'''

    def __init__(self, root, user: User, files: FileManager, return_home):
        """Class constructor

        args:
            root:
                TKinter object that the view is contained in
            user:
                The selected user's User object
            files:
                FileManager object responsible for handling the file operations
            return_home:
                Method responsible for creating the user's home view
        """
        self._root = root
        self._frame = None
        self._user = user
        self._files = files
        self._return_home = return_home

        self._model_entry = None
        self._year_entry = None
        self._tailnumber_entry = None

        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    @property
    def selected_user(self):
        return self._user.username

    def _initialize(self):
        self._frame = ttk.Frame(self._root)
        title_label = ttk.Label(self._frame, text='New plane', font=(
            'Arial', 16))
        title_label.grid(row=0, column=0, columnspan=2)

        self._initialize_new_plane_fields()

        return_button = ttk.Button(
            self._frame, text='Return', command=self._return_home)
        return_button.grid(column=0, row=4)
        self._new_plane_enter_button = ttk.Button(
            master=self._frame, text='Add plane', command=self._new_plane)
        self._new_plane_enter_button.grid(column=1, row=4)

        self.pack()

    def _initialize_new_plane_fields(self):
        '''Initializes fields for entering the details of a new plane'''

        model_label = ttk.Label(master=self._frame, text='Model:')
        model_label.grid(column=0, row=1, sticky=constants.E)

        year_label = ttk.Label(
            master=self._frame, text='Year:')
        year_label.grid(column=0, row=2, sticky=constants.E)

        tailnumber_label = ttk.Label(master=self._frame, text='Tail number:')
        tailnumber_label.grid(column=0, row=3, sticky=constants.E)

        self._model_entry = ttk.Entry(master=self._frame)
        self._model_entry.grid(column=1, row=1)

        self._year_entry = ttk.Entry(master=self._frame)
        self._year_entry.grid(column=1, row=2)

        self._tailnumber_entry = ttk.Entry(master=self._frame)
        self._tailnumber_entry.grid(column=1, row=3)

    def _initialize_error(self, error_text: str):
        '''Initializes an error text if an error is detected in the info entry fields

        args:
            error_text:
                The error text that should be displayed
        '''
        if self._error_label:
            self._error_label.destroy()
        self._error_label = ttk.Label(
            master=self._frame, text='Error: ' + error_text)
        self._error_label.grid(columnspan=2)
        self._error_label.configure(foreground='red')

    def _new_plane(self):
        if self._model_entry and self._year_entry:
            model = str(self._model_entry.get())
            if len(model) == 0:
                self._initialize_error('Plane model field must not be empty')
                return
            if len(model) > 100:
                self._initialize_error('Plane model too long')
                return

            year = self._year_entry.get()
            try:
                year = int(year)
            except ValueError:
                self._initialize_error('Year must be a number')
                return

            tailnumber = str(self._tailnumber_entry.get())
            if len(tailnumber) == 0:
                self._initialize_error('Tailnumber field must not be empty')
                return
            if len(tailnumber) > 10:
                self._initialize_error('Tailnumber too long')
                return

            self._files.save_new_plane(self._user, model, year, tailnumber)
            self._return_home()
