import os
import random
import glob
import time

# Path to the folder containing your video files
video_folder = '/path/to/your/video/folder'

# Delay between video playback (in seconds)
delay_between_videos = 10

while True:
    # Get a list of video files in the folder
    video_files = glob.glob(os.path.join(video_folder, '*.mp4'))

    # Check if there are any video files in the folder
    if not video_files:
        print("No video files found in the folder.")
    else:
        # Choose a random video file from the list
        random_video = random.choice(video_files)

        # Use omxplayer to play the selected video in full-screen mode
        os.system(f'omxplayer -o hdmi --aspect-mode fill "{random_video}"')

    # Wait for the specified delay before playing the next video
    time.sleep(delay_between_videos)