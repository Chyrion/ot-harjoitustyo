from tkinter import Tk
from ui.ui import UI
from datamanager.filemanager import FileManager


def main():
    window = Tk()
    window.title('Flightsim Logs Application')
    files = FileManager()
    users = files.userlist
    ui_view = UI(window, users, files)
    ui_view.start()

    window.mainloop()


if __name__ == '__main__':
    main()
