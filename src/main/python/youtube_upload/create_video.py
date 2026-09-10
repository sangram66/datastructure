import os, sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/moviepy')
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/ffmpeg')
import moviepy.editor as mp
mp.ffmpeg_tools.FFMPEG_BINARY = "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/ffmpeg"
from moviepy.editor import VideoFileClip, AudioFileClip, afx

def create_video(stock_video, audio_path, output_file="final_video.mp4", duration=10):
    try:
        video = VideoFileClip(stock_video).subclip(0, min(duration, VideoFileClip(stock_video).duration))
        audio = AudioFileClip(audio_path)

        if audio.duration < video.duration:
            video = video.set_audio(audio.fx(afx.audio_loop, duration=video.duration))
        else:
            video = video.set_audio(audio)

        video.write_videofile(output_file, fps=24, codec="libx264")
        print(f"Video created successfully: {output_file}")

    except FileNotFoundError:
        print(f"Error: One or more files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
create_video("/Users/sangrammallick/Documents/datastructure/stock_videos/253436_tiny.mp4", "/Users/sangrammallick/Documents/datastructure/voiceover.wav")