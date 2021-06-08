from pytube import YouTube

yt = YouTube('https://youtu.be/uyaCHgUfXN0').streams.first().audio_codec.
#yt = YouTube('https://www.youtube.com/watch?v=uyaCHgUfXN0')
print(yt)
#yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()