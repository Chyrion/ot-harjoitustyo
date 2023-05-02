from tkinter import ttk, constants
from datamanager.filemanager import FileManager
from entities.user import User


class UIUserNewFlightPlan:
    '''Responsible for creating a view for adding new flight log entries'''

    def __init__(self, root, user: User, files: FileManager, return_home):
        self._root = root
        self._frame = None
        self._user = user
        self._files = files
        self._return_home = return_home

        self._start_entry = None
        self._dest_entry = None

        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.grid(sticky=constants.NSEW)

    def destroy(self):
        self._frame.destroy()

    @property
    def selected_user(self):
        return self._user

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        title_label = ttk.Label(
            self._frame, text='New flight plan', font=('Arial', 16))
        title_label.grid(row=0, column=0, columnspan=2)

        self._initialize_new_flightplan_fields()

        enter_button = ttk.Button(
            self._frame, text='Add', command=self._new_flightplan)
        enter_button.grid(column=1, row=3)

        return_button = ttk.Button(
            self._frame, text='Return', command=self._return_home)
        return_button.grid(column=0, row=3)

        self.pack()

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

    def _initialize_new_flightplan_fields(self):
        start_entry_label = ttk.Label(master=self._frame, text='Start ICAO:')
        start_entry_label.grid(row=1, column=0)
        self._start_entry = ttk.Entry(master=self._frame)
        self._start_entry.grid(row=1, column=1)

        dest_entry_label = ttk.Label(
            master=self._frame, text='Destination ICAO:')
        dest_entry_label.grid(row=2, column=0)
        self._dest_entry = ttk.Entry(master=self._frame)
        self._dest_entry.grid(row=2, column=1)

    def _new_flightplan(self):
        if self._start_entry and self._dest_entry:
            start = self._start_entry.get()
            if len(start) != 4:
                self._initialize_error('Start ICAO should be 4 characters')
                return
            dest = self._dest_entry.get()
            if len(dest) != 4:
                self._initialize_error(
                    'Destination ICAO should be 4 characters')
                return

            self._files.save_new_flightplan(self._user, start, dest)
            self._return_home()
