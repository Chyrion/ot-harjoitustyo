from tkinter import ttk, constants
from entities.user import User
import datetime


class UIUserHomeview:
    """Responsible for creating the home page for a user"""

    def __init__(self, root, user: User, handle_new_flight, handle_change_user, handle_user_info):
        self._root = root
        self._frame = None
        self._user = user
        self._handle_new_flight = handle_new_flight
        self._handle_change_user = handle_change_user
        self._handle_user_info = handle_user_info

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        name_label = ttk.Label(
            master=self._frame, text=self._user.username).grid(column=0, row=0)

        new_flight_button = ttk.Button(
            master=self._frame, text='New flight', command=self._handle_new_flight).grid(column=1, row=0)

        userinfo_button = ttk.Button(
            master=self._frame, text='User info', command=self._handle_user_info
        ).grid(column=2, row=0)

        changeuser_button = ttk.Button(
            master=self._frame, text='Change user', command=self._handle_change_user
        ).grid(column=3, row=0)

        self._initialize_flight_log()

        self.pack()

    def _initialize_flight_log(self):
        """Initializes widgets for each flight that the user has saved"""

        if len(self._user.flights) != 0:
            flights = self._user.flights
            curr_row = 1
            for flight in flights:
                flight_date = datetime.datetime.fromisoformat(
                    str(flight.flight_date))
                label_title = ttk.Label(
                    master=self._frame, text='Flight', font=("Arial", 16)).grid(column=0, columnspan=4)

                label_date_text = ttk.Label(master=self._frame, text='Date').grid(
                    column=0, row=curr_row+1, sticky=constants.N)
                label_start_text = ttk.Label(
                    master=self._frame, text='Start').grid(column=1, row=curr_row+1, sticky=constants.N)
                label_destination_text = ttk.Label(
                    master=self._frame, text='Destination').grid(column=2, row=curr_row+1, sticky=constants.N)
                label_duration_text = ttk.Label(master=self._frame, text='Duration').grid(
                    column=3, row=curr_row+1, sticky=constants.N)

                label_date = ttk.Label(
                    master=self._frame, text=f'{flight_date.day} {flight_date.strftime("%B")} {flight_date.year}').grid(column=0, row=curr_row+2, sticky=constants.N)

                label_start_location = ttk.Label(
                    master=self._frame, text=flight.start).grid(column=1, row=curr_row+2, sticky=constants.N)

                label_destination_location = ttk.Label(
                    master=self._frame, text=flight.destination).grid(column=2, row=curr_row+2, sticky=constants.N)

                label_duration = ttk.Label(master=self._frame, text=f'{flight.duration} h').grid(
                    column=3, row=curr_row+2, sticky=constants.N)

                curr_row += 4

        else:
            label = ttk.Label(master=self._frame, text='No flights found')
            label.grid(row=1, column=0)
