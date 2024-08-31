import yt_dlp

# It is very important to use the latest version of yt_dlp.
# With the latest version, you are less likely to run into various issues.
# Latest version: "python -m pip install -U yt-dlp"

# Configuration
your_name = 'Josh'
download_audio = False  # Set to True to download audio only.
download_video = True  # Set to True to download video (with audio).
do_I_have_FFmpeg = False  # Set to True if you have FFmpeg on your computer.
what_video_quality = '144p'  # These are the options (only used with FFmpeg):
# 'best', '1080p', '720p', '480p', '360p', '240p', '144p', 'worst'
# The above options are used if available, otherwise a lower quality will
# be downloaded.

# FFmpeg is optional but strongly recommended. I installed it from:
# https://www.gyan.dev/ffmpeg/builds/
# I selected "ffmpeg-release-essentials.zip"
# If you install FFmpeg, and let yt_dlp know where it is, you won't get
# the annoying FFmpeg warning message. However, I don't know if you can install
# FFmpeg on Android.
# When using FFmpeg, it seems we can get better video quality.
# If you don't have FFmpeg, or are using this code on your phone, you must set
# "Do_I_have_FFmpeg" to False.

ffmpeg_path = 'C:\\Code\\ffmpeg-7.0.2-essentials_build\\bin\\ffmpeg.exe'

# This code can be used on phone as well with Pydroid 3.
# Just use line below as an example.
# output_dir = '/storage/emulated/0/Documents/MusicFromYT_Phone/AE'

output_dir = 'C:\\Code\\Python\\GitHub\\YT-DLP-Example'

# Example video URLs I want to download:
video_urls = [
    # 'https://youtu.be/_o-XIryB2gg?si=KugFTg0Rl2EEYJYA',
    # 'https://youtu.be/ca48oMV59LU?si=AmHT5onKmFq0N7ZW',
    # 'https://youtu.be/y26J3T3WT0I?si=XFX70dhYu0jVE6LZ',
    # 'https://youtu.be/gMQv5i3wQeQ?si=HhCtKmUnhfc3MDU2',
    'https://www.youtube.com/watch?v=PV6xELjHnf4',
    'https://youtube.com/shorts/l_U9MOWVmpo?si=aYrmA5tnugEIlr03',
]

# Audio download options
if do_I_have_FFmpeg:
    ydl_opts_audio = {
        'format': 'bestaudio/best',
        'outtmpl': output_dir + '/%(title)s.%(ext)s',
        'ffmpeg_location': ffmpeg_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }]
    }
else:
    ydl_opts_audio = {
        'format': 'm4a/best',
        'outtmpl': output_dir + '/%(title)s.%(ext)s',
    }

quality = ''
if what_video_quality == 'best':
    quality = 'bestvideo'
elif what_video_quality == '1080p':
    quality = 'bestvideo[height<=1080]'
elif what_video_quality == '720p':
    quality = 'bestvideo[height<=720]'
elif what_video_quality == '480p':
    quality = 'bestvideo[height<=480]'
elif what_video_quality == '360p':
    quality = 'bestvideo[height<=360]'
elif what_video_quality == '240p':
    quality = 'bestvideo[height<=240]'
elif what_video_quality == '144p':
    quality = 'bestvideo[height<=144]'
elif what_video_quality == 'worst':
    quality = 'worstvideo'
else:  # User fail
    quality = 'bestvideo[height<=720]'

if do_I_have_FFmpeg:
    ydl_opts_video = {
        'format': f'{quality}+bestaudio',
        'outtmpl': output_dir + '/%(title)s.%(ext)s',
        'ffmpeg_location': ffmpeg_path,
    }
    ydl_opts_video_fallback = {
        'format': 'worstvideo+bestaudio',
        'outtmpl': output_dir + '/%(title)s.%(ext)s',
        'ffmpeg_location': ffmpeg_path,
    }
else:
    ydl_opts_video = {
        'format': 'mp4/best',
        'outtmpl': output_dir + '/%(title)s.%(ext)s',
    }
    ydl_opts_video_fallback = {
        'format': 'mp4/best',
        'outtmpl': output_dir + '/%(title)s.%(ext)s',
    }

print(f'\nHello {your_name}!!!\n')

# Download audio only
if download_audio:
    print("Downloading audio only...")
    with yt_dlp.YoutubeDL(ydl_opts_audio) as ydl_a:
        for video_url in video_urls:
            ydl_a.download([video_url])

# Download video (with audio)
if download_video:
    print("Downloading video with audio...")
    with yt_dlp.YoutubeDL(ydl_opts_video) as ydl_v:
        for video_url in video_urls:
            try:
                ydl_v.download([video_url])
            except Exception as e:
                print(f"An error occurred while downloading {video_url} with requested quality: {e}")
                print(f"Retrying with fallback quality (worst available)")
                try:
                    with yt_dlp.YoutubeDL(ydl_opts_video_fallback) as ydl_v_fallback:
                        ydl_v_fallback.download([video_url])
                except Exception as e:
                    print(f"An error occurred while downloading {video_url} with fallback quality: {e}")

print('\nNice! That is amazing!!!')
