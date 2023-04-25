from tkinter import ttk, constants, StringVar
from tkcalendar import DateEntry
from datamanager.filemanager import FileManager
from entities.user import User


class UIUserNewFlight:
    '''Responsible for creating a view for adding new flight log entries'''

    def __init__(self, root, user: User, files: FileManager, return_home):
        self._root = root
        self._frame = None
        self._user = user
        self._files = files
        self._return_home = return_home

        self._new_flight_start_entry = None
        self._new_flight_dest_entry = None
        self._new_flight_duration_entry = None
        self._new_flight_date_entry = None
        self._new_flight_plane_entry = None

        self.plane_var = StringVar
        self._planelist = []

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
        for plane in self._user.planes:
            self._planelist.append(plane['tailnumber'])
        self._planelist = tuple(self._planelist)
        self._frame = ttk.Frame(master=self._root)
        title_label = ttk.Label(
            master=self._frame, text='New flight', font=('Arial', 16))
        title_label.grid(columnspan=2)
        self._initialize_new_flight_fields()

        self.pack()

    def _initialize_new_flight_fields(self):
        """Initializes data entry fields for entering details of a flight"""
        entryvar = StringVar()

        start_label = ttk.Label(master=self._frame, text='Start ICAO:')
        start_label.grid(column=0, row=1, sticky=constants.E)

        destination_label = ttk.Label(
            master=self._frame, text='Destination ICAO:')
        destination_label.grid(column=0, row=2, sticky=constants.E)

        duration_label = ttk.Label(master=self._frame, text='Duration:')
        duration_label.grid(column=0, row=3, sticky=constants.E)

        date_label = ttk.Label(master=self._frame, text='Date:')
        date_label.grid(column=0, row=4, sticky=constants.E)

        plane_label = ttk.Label(self._frame, text='Plane:').grid(
            column=0, row=5, sticky=constants.E)

        self._new_flight_start_entry = ttk.Entry(master=self._frame)
        self._new_flight_start_entry.grid(column=1, row=1)

        self._new_flight_dest_entry = ttk.Entry(master=self._frame)
        self._new_flight_dest_entry.grid(column=1, row=2)

        self._new_flight_duration_entry = ttk.Entry(master=self._frame)
        self._new_flight_duration_entry.grid(column=1, row=3)

        self._new_flight_date_entry = DateEntry(master=self._frame)
        self._new_flight_date_entry.grid(column=1, row=4)

        # OptionMenu is not being nice, so it'll have to wait
        # if len(self._planelist) > 0:
        #     self._new_flight_plane_entry = ttk.OptionMenu(
        #         master=self._frame, variable=entryvar, default=self._planelist[0], *self._planelist).grid(column=1, row=5)
        self._new_flight_plane_entry = ttk.Label(
            self._frame, text='Plane selection unavailable').grid(column=1, row=5)

        self._new_flight_enter_button = ttk.Button(
            master=self._frame, text='Add flight', command=self._new_flight)
        self._new_flight_enter_button.grid(columnspan=2)

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

    def _new_flight(self):
        if self._new_flight_dest_entry and self._new_flight_start_entry:

            start = self._new_flight_start_entry.get()
            if len(start) != 4:
                self._initialize_error('Start ICAO should be 4 characters')
                return

            dest = self._new_flight_dest_entry.get()
            if len(dest) != 4:
                self._initialize_error(
                    'Destination ICAO should be 4 characters')
                return

            duration = self._new_flight_duration_entry.get()
            try:
                duration = float(duration)
            except ValueError:
                self._initialize_error('Duration is not a number')
                return

            date = self._new_flight_date_entry.get_date()

            # if not self._plane:
            #     self._initialize_error('No plane selected!')
            #     return

            self._files.save_new_flight(
                self._user, start, dest, duration, date)
            self._return_home()
