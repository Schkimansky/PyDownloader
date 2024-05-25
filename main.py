from pytube import YouTube

def download_youtube_video(url, save_path='.'):
    try:
        yt = YouTube(url)
        
        stream = yt.streams.get_highest_resolution()
        
        stream.download(output_path=save_path)
        
        print(f"Video downloaded successfully and saved to {save_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

video_url = input('(Make sure that when you enter a url, Get the url by clicking the share button on youtube. Only links such as youtu.be are valid, Not the browser url you copied.) \n\n Enter URL: ')
save_path = '.' # "." is recommended because it saves the vidio in the current folder.

download_youtube_video(video_url)
