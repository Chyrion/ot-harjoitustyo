from tkinter import ttk, constants
from datamanager.filemanager import FileManager


class UIUserHomeview:
    """Responsible for creating the home page for a user"""

    def __init__(self, root, username: str, files: FileManager):
        self._root = root
        self._frame = None
        self._username = username
        self._files = files
        self._flights = []

        self._userdata = self._load_data()
        self._new_flight_start_entry = None
        self._new_flight_dest_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        name_label = ttk.Label(
            master=self._root, text=self._userdata['username'])
        name_label.pack()
        self._initialize_flight_log()
        self._new_flight_start_entry = ttk.Entry(
            master=self._frame)
        self._new_flight_start_entry.grid(padx=5, pady=2)
        self._new_flight_dest_entry = ttk.Entry(
            master=self._frame)
        self._new_flight_dest_entry.grid(padx=5, pady=2)
        self._new_flight_enter_button = ttk.Button(
            master=self._frame, text='Add flight', command=self._new_flight)
        self._new_flight_enter_button.grid(padx=5, pady=2)

        # self._initialize_new_flight_fields()

        self.pack()

    def _initialize_flight_log(self):
        """Initializes widgets for each flight that the user has saved"""

        if len(self._userdata['flights']) != 0:
            flights = self._userdata['flights']

            for flight in flights:
                label_title = ttk.Label(
                    master=self._frame, text='Flight', font=("Arial", 16)).grid(padx=5, pady=5)
                label_start = ttk.Label(
                    master=self._frame, text=('Start: '+flight['start'])).grid(padx=5, pady=5)
                label_destination = ttk.Label(
                    master=self._frame, text=('Destination: '+flight['destination'])).grid(padx=5, pady=5)
                self._flights.append(
                    (label_title, label_start, label_destination))

        else:
            label = ttk.Label(master=self._frame, text='No flights found')
            label.grid(row=1, column=0)

    def _initialize_new_flight_fields(self):
        """Initializes text fields and button to enter a new flight"""

        self._new_flight_start_entry = ttk.Entry(
            master=self._frame).grid(padx=5, pady=2)
        self._new_flight_dest_entry = ttk.Entry(
            master=self._frame).grid(padx=5, pady=2)
        self._new_flight_enter_button = ttk.Button(
            master=self._frame, text='Add flight', command=self._new_flight).grid(padx=5, pady=2)

    def _new_flight(self):
        print('saving new flight')
        print(self._new_flight_start_entry)
        print(self._new_flight_dest_entry)
        if self._new_flight_dest_entry and self._new_flight_start_entry:
            start = self._new_flight_start_entry.get()
            dest = self._new_flight_dest_entry.get()
            self._files.save_new_flight(self._username, start, dest)

    def _load_data(self):
        return self._files.load_user_data(self._username)
