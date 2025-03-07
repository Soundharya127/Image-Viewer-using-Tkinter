import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("700x500")
        self.root.resizable(True, True)

        # Label to display images
        self.image_label = tk.Label(root, bg="gray")
        self.image_label.pack(expand=True, fill=tk.BOTH)

        # Frame for buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill=tk.X, side=tk.BOTTOM)

        # Open Folder button
        self.open_button = tk.Button(self.button_frame, text="Open Folder", command=self.load_images)
        self.open_button.pack(side=tk.TOP, padx=10, pady=10)

        # Previous button
        self.prev_button = tk.Button(self.button_frame, text="Previous", command=self.prev_image, state=tk.DISABLED)
        self.prev_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Next button
        self.next_button = tk.Button(self.button_frame, text="Next", command=self.next_image, state=tk.DISABLED)
        self.next_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Exit button
        self.exit_button = tk.Button(self.button_frame, text="Exit", command=root.quit)
        self.exit_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        # Variables for images
        self.image_list = []
        self.current_index = 0

    def load_images(self):
        """Load images from the selected folder."""
        folder_selected = filedialog.askdirectory()
        if not folder_selected:
            messagebox.showwarning("Warning", "No folder selected!")
            return

        # Get all image files from the folder
        self.image_list = [os.path.join(folder_selected, f) for f in os.listdir(folder_selected)
                           if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

        if self.image_list:
            self.current_index = 0
            self.display_image()
            self.update_buttons()
        else:
            messagebox.showerror("Error", "No images found in the selected folder!")

    def display_image(self):
        """Display the current image."""
        if not self.image_list:
            return

        image_path = self.image_list[self.current_index]
        image = Image.open(image_path)
        image = image.resize((600, 450), Image.Resampling.LANCZOS)  # Resize the image
        photo = ImageTk.PhotoImage(image)

        self.image_label.config(image=photo)
        self.image_label.image = photo

    def next_image(self):
        """Show the next image in the list."""
        if self.current_index < len(self.image_list) - 1:
            self.current_index += 1
            self.display_image()
        self.update_buttons()

    def prev_image(self):
        """Show the previous image in the list."""
        if self.current_index > 0:
            self.current_index -= 1
            self.display_image()
        self.update_buttons()

    def update_buttons(self):
        """Enable or disable navigation buttons based on index."""
        self.prev_button.config(state=tk.NORMAL if self.current_index > 0 else tk.DISABLED)
        self.next_button.config(state=tk.NORMAL if self.current_index < len(self.image_list) - 1 else tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()
