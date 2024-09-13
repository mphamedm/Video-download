import yt_dlp

video_url = input("enter url : ")
ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
    print("finsh download")
    
    

