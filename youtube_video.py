import pytube
import os
from pytube import YouTube


def download_youtube_video(youtube_url):
    """Downloads a YouTube video, renames it to the first three characters, and returns the downloaded file path."""

    try:
        # Create a YouTube object
        yt = pytube.YouTube(youtube_url)

        # Get the highest resolution progressive stream
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        # Download the video
        print("Downloading...")
        video.download()

        # Get the original filename
        original_filename = video.default_filename

        # Extract the first three characters and keep the file extension
        new_filename = original_filename[:12] + os.path.splitext(original_filename)[1]

        # Rename the downloaded file
        os.rename(original_filename, new_filename)

        print("Download complete! Video saved to:", new_filename)
        return new_filename

    except Exception as e:
        print("An error occurred:", e)
        return None
