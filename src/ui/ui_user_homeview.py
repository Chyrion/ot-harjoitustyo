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
        self._frame.columnconfigure(0, weight=2)
        self._frame.columnconfigure(1, weight=1)

        name_label = ttk.Label(
            master=self._frame, text=self._userdata['username'])
        name_label.grid(column=0, row=0, padx=5, pady=5)
        new_flight_button = ttk.Button(
            master=self._frame, text='New flight', command=self._handle_new_flight)
        new_flight_button.grid(column=1, row=0, padx=5, pady=5)
        self._initialize_flight_log()

        self.pack()

    def _initialize_flight_log(self):
        """Initializes widgets for each flight that the user has saved"""

        if len(self._userdata['flights']) != 0:
            flights = self._userdata['flights']
            curr_row = 1
            for flight in flights:
                label_title = ttk.Label(
                    master=self._frame, text='Flight', font=("Arial", 16)).grid(column=0, row=curr_row)
                label_start_text = ttk.Label(
                    master=self._frame, text='Start:').grid(column=0, row=curr_row+1)
                label_start_location = ttk.Label(
                    master=self._frame, text=flight['start']).grid(column=1, row=curr_row+1)

                label_destination_text = ttk.Label(
                    master=self._frame, text='Destination: ').grid(column=0, row=curr_row+2)
                label_destination_location = ttk.Label(
                    master=self._frame, text=flight['destination']).grid(column=1, row=curr_row+2)
                curr_row += 3

        else:
            label = ttk.Label(master=self._frame, text='No flights found')
            label.grid(row=1, column=0)

    def _load_data(self):
        return self._files.load_user_data(self._username)
