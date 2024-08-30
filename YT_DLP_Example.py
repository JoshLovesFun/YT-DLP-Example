import yt_dlp

print('Hello Josh!')
print('')

video_urls = [
    # 'https://youtu.be/_o-XIryB2gg?si=KugFTg0Rl2EEYJYA',
    # 'https://youtu.be/ca48oMV59LU?si=AmHT5onKmFq0N7ZW',
    # 'https://youtu.be/y26J3T3WT0I?si=XFX70dhYu0jVE6LZ',
    # 'https://youtu.be/gMQv5i3wQeQ?si=HhCtKmUnhfc3MDU2',
    'https://youtu.be/0bmE9XY3sOc?si=fzVi7YrDT6SRKSwP',
    'https://youtube.com/shorts/l_U9MOWVmpo?si=aYrmA5tnugEIlr03',
]

# This can be used on phone as well with Pydroid 3.
# Just use line below as example.
# output_dir = '/storage/emulated/0/Documents/MusicFromYT_Phone/AE'
output_dir = 'C:\\Code\\Python\\GitHub\\YT-DLP-Example'

# Audio
ydl_opts_audio = {
    'format': 'm4a/best',
    'outtmpl': output_dir + '/%(title)s.%(ext)s',
}

# Video
ydl_opts_video = {
    'format': 'mp4/best',
    'outtmpl': output_dir + '/%(title)s.%(ext)s',
}

# Download audio only
with yt_dlp.YoutubeDL(ydl_opts_audio) as ydl_a:
    for video_url in video_urls:
        ydl_a.download([video_url])

# Download video (with audio)
with yt_dlp.YoutubeDL(ydl_opts_video) as ydl_v:
    for video_url in video_urls:
        ydl_v.download([video_url])

print('')
print('Nice!')
print('')
print('That is amazing!!!')
