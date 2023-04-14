from tkinter import ttk, constants
from datamanager.filemanager import FileManager


class UIUserNewFlight:
    '''Responsible for creating a view for adding new flight log entries'''

    def __init__(self, root, username: str, files: FileManager, return_home):
        self._root = root
        self._frame = None
        self._username = username
        self._files = files
        self._return_home = return_home

        self._new_flight_start_entry, self._new_flight_dest_entry = None, None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    @property
    def selected_user(self):
        return self._username

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        title_label = ttk.Label(
            master=self._frame, text='New flight', font=('Arial', 16))
        title_label.grid(padx=5, pady=5)
        self._initialize_new_flight_fields()

        self.pack()

    def _initialize_new_flight_fields(self):
        """Initializes text fields and button to enter a new flight"""

        self._new_flight_start_entry = ttk.Entry(master=self._frame)
        self._new_flight_start_entry.grid(padx=5, pady=2)

        self._new_flight_dest_entry = ttk.Entry(master=self._frame)
        self._new_flight_dest_entry.grid(padx=5, pady=2)

        self._new_flight_enter_button = ttk.Button(
            master=self._frame, text='Add flight', command=self._new_flight)
        self._new_flight_enter_button.grid(padx=5, pady=2)

    def _new_flight(self):
        print('saving new flight')
        if self._new_flight_dest_entry and self._new_flight_start_entry:
            start = self._new_flight_start_entry.get()
            dest = self._new_flight_dest_entry.get()
            self._files.save_new_flight(self._username, start, dest)
            self._return_home()
