import tkinter as tk
import os
import subprocess

def start_drag(event):
    global x, y
    x = event.x
    y = event.y

def drag(event):
    root.geometry(f'+{event.x_root - x}+{event.y_root - y}')

def open_image():
    new_image_name = 'StartButtonBackgroundTexture2.png'
    new_image_path = os.path.join(current_directory, folder_path, new_image_name)
    
    if os.path.isfile(new_image_path):
        try:
            subprocess.Popen(['xdg-open', new_image_path])  # Open the image using default viewer on Linux
        except OSError:
            try:
                subprocess.Popen(['open', new_image_path])  # Open the image using default viewer on macOS
            except OSError:
                subprocess.Popen(['start', new_image_path], shell=True)  # Open the image using default viewer on Windows
    else:
        print(f"Error: The file {new_image_name} does not exist in the directory {os.path.join(current_directory, folder_path)}")

# Create the main window
root = tk.Tk()
root.title("Open Image")

# Remove the window border and title bar
root.overrideredirect(True)

# Load the initial image using the folder structure
image_name = 'StartButtonBackgroundTexture.png'
folder_path = 'Textures'
current_directory = os.path.dirname(__file__)  # Get current script directory
image_path = os.path.join(current_directory, folder_path, image_name)

# Check if the main image file exists
if not os.path.isfile(image_path):
    print(f"Error: The file {image_name} does not exist in the directory {os.path.join(current_directory, folder_path)}")
    root.destroy()  # Close the Tkinter window
else:
    photo = tk.PhotoImage(file=image_path)

    # Create a label to display the main image
    label = tk.Label(root, image=photo, borderwidth=0, highlightthickness=0)
    label.pack()

    # Bind mouse events to the label for dragging
    label.bind('<Button-1>', start_drag)
    label.bind('<B1-Motion>', drag)

    # Load the button image for the top-right corner button
    button_image_name_top = 'CloseBackgroundStartExit.png'
    button_image_path_top = os.path.join(current_directory, folder_path, button_image_name_top)

    # Check if the button image file exists for the top-right corner button
    if not os.path.isfile(button_image_path_top):
        print(f"Error: The file {button_image_name_top} does not exist in the directory {os.path.join(current_directory, folder_path)}")
    else:
        button_photo_top = tk.PhotoImage(file=button_image_path_top)

        # Create the top-right corner button
        button_top = tk.Button(root, image=button_photo_top, borderwidth=0, highlightthickness=0, command=root.quit)
        button_top.place(relx=1.0, rely=0.0, anchor='ne')  # Place button at the top-right corner

    # Load the button image for the middle button
    button_image_name_middle = 'StartButtonTexsture.png'  # Corrected filename here
    button_image_path_middle = os.path.join(current_directory, folder_path, button_image_name_middle)

    # Check if the button image file exists for the middle button
    if not os.path.isfile(button_image_path_middle):
        print(f"Error: The file {button_image_name_middle} does not exist in the directory {os.path.join(current_directory, folder_path)}")
    else:
        button_photo_middle = tk.PhotoImage(file=button_image_path_middle)

        # Create the middle button
        button_middle = tk.Button(root, image=button_photo_middle, borderwidth=0, highlightthickness=0, command=open_image)
        button_middle.place(relx=0.5, rely=0.5, anchor='center')  # Place button in the center of the window

# Start the GUI event loop
root.mainloop()
