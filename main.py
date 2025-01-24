from src.all_imports import * 
from src.window import configure_window, create_main_screen_activity_01, create_main_screen_activity_02, create_main_screen_activity_03
from src.util import configure_close_behavior

sys.dont_write_bytecode = True

window = tk.Tk()
configure_window(window)

main_frame = tk.Frame(window, bg="#2e3b4e")
main_frame.pack(fill="both", expand=True)

create_main_screen_activity_01(window, main_frame)

configure_close_behavior(window)

window.mainloop()