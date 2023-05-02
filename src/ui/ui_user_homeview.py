import datetime
from tkinter import ttk, constants
from entities.user import User


class UIUserHomeview:
    """Responsible for creating the home page for a user"""

    def __init__(self, root, user: User, handle_new_flight, handle_change_user, handle_user_info, handle_new_flightplan):
        self._root = root
        self._frame = None
        self._user = user
        self._handle_new_flight = handle_new_flight
        self._handle_change_user = handle_change_user
        self._handle_user_info = handle_user_info
        self._handle_new_flightplan = handle_new_flightplan

        self._curr_row = 1

        self._initialize()

    def pack(self):
        self._frame.grid(sticky=constants.NSEW)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        name_label = ttk.Label(
            master=self._frame, text=self._user.username).grid(column=0, row=0)

        new_flight_button = ttk.Button(
            master=self._frame, text='New flight', command=self._handle_new_flight).grid(column=1, row=0)

        new_flightplan_button = ttk.Button(
            self._frame, text='New flight plan', command=self._handle_new_flightplan).grid(column=2, row=0)

        userinfo_button = ttk.Button(
            master=self._frame, text='User info', command=self._handle_user_info
        ).grid(column=3, row=0)

        changeuser_button = ttk.Button(
            master=self._frame, text='Change user', command=self._handle_change_user
        ).grid(column=4, row=0)

        self._initialize_flight_log()
        self._initialize_flightplans()

        self.pack()

    def _initialize_flight_log(self):
        """Initializes widgets for each flight that the user has saved"""

        if len(self._user.flights) != 0:
            flights = self._user.flights
            for flight in flights:
                flight_date = datetime.datetime.fromisoformat(
                    str(flight.flight_date))
                label_title = ttk.Label(
                    master=self._frame, text='Flight', font=("Arial", 16)).grid(column=0, columnspan=4)

                label_date_text = ttk.Label(master=self._frame, text='Date').grid(
                    column=0, row=self._curr_row+1, sticky=constants.N)
                label_start_text = ttk.Label(
                    master=self._frame, text='Start').grid(column=1, row=self._curr_row+1, sticky=constants.N)
                label_destination_text = ttk.Label(
                    master=self._frame, text='Destination').grid(column=2, row=self._curr_row+1, sticky=constants.N)
                label_duration_text = ttk.Label(master=self._frame, text='Duration').grid(
                    column=3, row=self._curr_row+1, sticky=constants.N)

                label_date = ttk.Label(
                    master=self._frame, text=f'{flight_date.day} {flight_date.strftime("%B")} {flight_date.year}').grid(column=0, row=self._curr_row+2, sticky=constants.N)

                label_start_location = ttk.Label(
                    master=self._frame, text=flight.start).grid(column=1, row=self._curr_row+2, sticky=constants.N)

                label_destination_location = ttk.Label(
                    master=self._frame, text=flight.destination).grid(column=2, row=self._curr_row+2, sticky=constants.N)

                label_duration = ttk.Label(master=self._frame, text=f'{flight.duration} h').grid(
                    column=3, row=self._curr_row+2, sticky=constants.N)

                label_plane_text = ttk.Label(self._frame, text='Plane')
                label_plane_text.grid(
                    column=4, row=self._curr_row+1, sticky=constants.N)

                label_plane = ttk.Label(
                    self._frame, text=flight.plane.tailnumber)
                label_plane.grid(
                    column=4, row=self._curr_row+2, sticky=constants.N)

                self._curr_row += 4

        else:
            label = ttk.Label(master=self._frame, text='No flights found')
            label.grid(row=1, column=0)

    def _initialize_flightplans(self):
        if len(self._user.flightplans) != 0:
            for plan in self._user.flightplans:
                label_title = ttk.Label(
                    master=self._frame, text='Flight plan', font=("Arial", 16))
                label_title.grid(column=0, row=self._curr_row+1, columnspan=4)

                start_label_text = ttk.Label(self._frame, text='Start')
                start_label_text.grid(
                    column=0, columnspan=2, row=self._curr_row+2)

                dest_label_text = ttk.Label(self._frame, text='Start')
                dest_label_text.grid(
                    column=2, columnspan=2, row=self._curr_row+2)

                start_label = ttk.Label(self._frame, text=plan.start)
                start_label.grid(column=0, columnspan=2, row=self._curr_row+3)

                dest_label = ttk.Label(self._frame, text=plan.destination)
                dest_label.grid(column=2, columnspan=2, row=self._curr_row+3)

                self._curr_row += 4

        else:
            label = ttk.Label(self._frame, text='No flight plans found')
            label.grid(column=0)
