from pytube import YouTube

yt = YouTube(str(input("Enter the video link: ")))
audio = yt.streams.filter(only_audio=True).all()

s = 1
for v in audio:
    print(str(s)+". "+str(v))
    s += 1

n = int(input("Enter the number of the video: "))
vid = audio[n-1]

destination = str(input("Enter the destination: "))
vid.download(destination)

print("\nHas been successfully downloaded")