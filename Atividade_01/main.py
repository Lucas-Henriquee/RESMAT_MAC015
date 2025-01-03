import tkinter as tk
from window import configure_window, create_main_screen

window = tk.Tk()
configure_window(window)

main_frame = tk.Frame(window, bg="#2e3b4e")
main_frame.pack(fill="both", expand=True)

create_main_screen(window, main_frame)

window.mainloop()