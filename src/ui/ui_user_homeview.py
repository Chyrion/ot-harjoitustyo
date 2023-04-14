from tkinter import ttk, constants
from datamanager.filemanager import FileManager


class UIUserHomeview:
    """Responsible for creating the home page for a user"""

    def __init__(self, root, username: str, files: FileManager, handle_new_flight):
        self._root = root
        self._frame = None
        self._username = username
        self._files = files
        self._flights = []

        self._userdata = self._load_data()
        self._handle_new_flight = handle_new_flight

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        name_label = ttk.Label(
            master=self._frame, text=self._userdata['username'])
        name_label.grid(padx=5, pady=5)
        self._initialize_flight_log()
        new_flight_button = ttk.Button(
            master=self._frame, text='New flight', command=self._handle_new_flight)
        new_flight_button.grid(padx=5, pady=5)

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

    def _load_data(self):
        return self._files.load_user_data(self._username)
