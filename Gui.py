import yt_dlp
import webbrowser
from tkinter import Tk, Entry, Button, Label, messagebox , Frame

def play_video(resolution):
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please paste a valid YouTube link.")
        return
    try:
        ydl_opts = {}
        if resolution == "high":
            ydl_opts = {'format': 'bestvideo'}
        elif resolution == "low":
            ydl_opts = {'format': 'bestvideo'}
        elif resolution == "audio":
            ydl_opts = {'format': 'bestaudio'}
        else:
            messagebox.showerror("Error", "Invalid resolution option.")
            return
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info.get('url', None)
            if not video_url:
                messagebox.showerror("Error", f"No streams available for {resolution} resolution.")
            else:
                webbrowser.open(video_url)
    except yt_dlp.utils.DownloadError as e:
        messagebox.showerror("Download Error", f"Could not process the video: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

window = Tk()
window.title("Multimedia GUI")
window.config(bg="#2C3E50")

Label(window, text="Add Link Here", bg="#2C3E50", fg="#ECF0F1", font=("Arial", 12)).pack(pady=10)
url_entry = Entry(window, width=50, fg="#2C3E50", bg="#ECF0F1", font=("Arial", 12))
url_entry.pack(pady=10)

button_frame = Frame(window, bg="#2C3E50")
button_frame.pack(pady=10)

high_res_button = Button(button_frame, text="High Resolution", command=lambda: play_video("high"), bg="#E74C3C", fg="#ECF0F1", font=("Arial", 12))
high_res_button.pack(side="left", padx=10)

low_res_button = Button(button_frame, text="Low Resolution", command=lambda: play_video("low"), bg="#F39C12", fg="#ECF0F1", font=("Arial", 12))
low_res_button.pack(side="left", padx=10)

audio_button = Button(window, text="Audio Only", command=lambda: play_video("audio"), bg="#1ABC9C", fg="#ECF0F1", font=("Arial", 12))
audio_button.pack(pady=10)

window.mainloop()
