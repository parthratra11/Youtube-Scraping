from youtube_search import YoutubeSearch
from pytube import YouTube
import os

search=input('\nEnter the title of the song to be searched:'); print('')
result_count=int(input('Enter the no. of results to be shown:')); print('')

print('Choose a valid result count !') or quit() if result_count<1 else None

yt_search=YoutubeSearch(search, max_results=result_count).to_dict()

try:
    if result_count==1:
        download_path=input('Enter the download path:'); print('')

        yt_video=YouTube(f"https://www.youtube.com/{yt_search[0]['url_suffix']}").streams.filter(only_audio=True).first()
        main_file=yt_video.download(output_path=download_path)

        base_file, extension=os.path.splitext(main_file)
        temp_file=base_file+'.mp3'
        os.rename(main_file, temp_file)

    else:
        for result in range(result_count):
            print(f'{result+1}.', f"{yt_search[result]['title']} BY {yt_search[result]['channel']}")

        choice, download_path=int(input('\nEnter the index no. of the song to be downloaded:')), input('Enter the download path:'); print('')

        yt_video=YouTube(f"https://www.youtube.com/{yt_search[choice-1]['url_suffix']}").streams.filter(only_audio=True).first()
        main_file=yt_video.download(output_path=download_path)

        base_file, extension=os.path.splitext(main_file)
        temp_file=base_file+'.mp3'
        os.rename(main_file, temp_file)

    print(f'{yt_video.title} has been successfully downloaded\n')
    
except:
    print(f'An error has occured, {yt_video.title} could not be downloaded, Please check if the file already exists\n')