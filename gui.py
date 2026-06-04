import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import subprocess
import os
import threading
import platform
from tkinter import filedialog # Import filedialog for directory selection

def main():
    app = tk.Tk()
    app.geometry("500x550") # Increased height for new widgets
    app.title("Auto YouTube Downloader")
    
    # Find the icon relative to this script
    base_path = os.path.dirname(__file__)
    icon_path = os.path.join(base_path, "Share.ico")
    
    if os.path.exists(icon_path):
        image = Image.open(icon_path)
        photo = ImageTk.PhotoImage(image)
        # iconphoto is more cross-platform than iconbitmap
        app.iconphoto(True, photo)
        label = tk.Label(app, image=photo)
        label.image = photo
        label.pack()

    # Variables for dynamic content
    # Default to user's home directory for downloads
    download_path_var = tk.StringVar(value=os.path.expanduser("~")) 
    status_var = tk.StringVar(value="Ready to download!")

    def browse_directory():
        selected_directory = filedialog.askdirectory(initialdir=download_path_var.get())
        if selected_directory:
            download_path_var.set(selected_directory)

    def execute():
        url = vidurlent.get().strip()
        if not url:
            messagebox.showwarning("Warning", "Please enter a valid YouTube URL.")
            return

        # Disable button to prevent multiple clicks
        dwnldbtn.config(state=tk.DISABLED, text="Downloading...")
        status_var.set("Starting download...")
        
        def run_download():
            try:
                output_path = download_path_var.get()
                if not os.path.exists(output_path):
                    os.makedirs(output_path) # Create directory if it doesn't exist

                # Added --concurrent-fragments to speed up the download
                # Added --no-playlist to ensure only the specific video is downloaded
                subprocess.run([
                    "yt-dlp", 
                    "--concurrent-fragments", "10",
                    "--buffer-size", "16K",
                    "--no-mtime",
                    "--no-playlist", 
                    "-o", os.path.join(output_path, "%(title)s.%(ext)s"), # Output to selected path
                    url
                ], check=True)
                
                status_var.set("Download complete! Opening folder...")
                # Cross-platform way to open the download folder
                if platform.system() == "Windows":
                    os.startfile(output_path)
                elif platform.system() == "Darwin":  # macOS
                    subprocess.run(["open", output_path])
                else:  # Linux
                    subprocess.run(["xdg-open", output_path])
                
                status_var.set("Ready to download!")
                    
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Download failed: {e}\nCheck console for details.")
                status_var.set("Download failed!")
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")
                status_var.set("An error occurred!")
            finally:
                # Re-enable the button
                dwnldbtn.config(state=tk.NORMAL, text="Download")

        # Run download in a separate thread so the GUI doesn't freeze
        threading.Thread(target=run_download, daemon=True).start()

    lbl = tk.Label(app, text="Auto YouTube Downloader", font=("Arial", 20))
    lbl.pack(pady=20)
    vidurllbl = tk.Label(app, text="Enter Video URL:", font=("Arial", 14))
    vidurllbl.pack(pady=10)
    vidurlent = tk.Entry(app, width=40, font=("Arial", 12))
    vidurlent.pack(pady=5)
    dwnldbtn = tk.Button(app, text="Download", font=("Arial", 14), command=execute)
    dwnldbtn.pack(pady=20)

    # Download Path widgets
    path_frame = tk.Frame(app)
    path_frame.pack(pady=10)
    
    path_lbl = tk.Label(path_frame, text="Download to:", font=("Arial", 12))
    path_lbl.pack(side=tk.LEFT, padx=5)
    
    path_entry = tk.Entry(path_frame, textvariable=download_path_var, width=30, font=("Arial", 12))
    path_entry.pack(side=tk.LEFT, padx=5)
    
    browse_btn = tk.Button(path_frame, text="Browse...", command=browse_directory)
    browse_btn.pack(side=tk.LEFT, padx=5)

    # Status Label
    status_lbl = tk.Label(app, textvariable=status_var, font=("Arial", 10), fg="blue")
    status_lbl.pack(pady=5)

    app.mainloop()

if __name__ == "__main__":
    main()