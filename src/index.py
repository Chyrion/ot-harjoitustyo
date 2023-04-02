from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title('Flightsim Logs Application')

    users = ['Chyrion', 'User1', 'Pilot']
    ui_view = UI(window, users)
    ui_view.start()

    window.mainloop()


if __name__ == '__main__':
    main()
