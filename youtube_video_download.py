from youtube_search import YoutubeSearch
from pytube import YouTube
import webbrowser

search=input('\nEnter the title of the video to be searched:')
result_count=int(input('\nEnter the no. of results to be shown:'))
video_resolution=input('\nEnter the desired resolution for the downloaded video:')

print('Choose a valid result count !') or quit() if result_count<1 else None

yt_search=YoutubeSearch(search, max_results=result_count).to_dict()

def youtube_video_check(temp_choice):
    check_var=input('\nDo you want to watch the selected video before downloading it? (Y/N):')

    if check_var=='Y' or check_var=='y':
        webbrowser.open(f"https://www.youtube.com/{yt_search[temp_choice]['url_suffix']}")

        recheck_var=input('\nDo you wish to download the selected video? (Y/N):')
        None if recheck_var=='Y' or recheck_var=='y' else print('') or quit()    

try:
    if result_count==1:
        yt_video=YouTube(f"https://www.youtube.com/{yt_search[0]['url_suffix']}").streams.filter(res=str(video_resolution), mime_type='video/webm').first()
        youtube_video_check(0)

        download_path=input('\nEnter the download path:'); print('')
        main_file=yt_video.download(output_path=download_path)

    else:
        print('')

        for result in range(result_count):
            print(f'{result+1}.', f"{yt_search[result]['title']} BY {yt_search[result]['channel']}")

        choice=int(input('\nEnter the index no. of the video to be downloaded:'))

        yt_video=YouTube(f"https://www.youtube.com/{yt_search[choice-1]['url_suffix']}").streams.filter(res=str(video_resolution), mime_type='video/webm').first()
        youtube_video_check(choice-1)

        download_path=input('\nEnter the download path:'); print('')
        main_file=yt_video.download(output_path=download_path)

    print(f'{yt_video.title} has been successfully downloaded\n')
    
except Exception as e:
    print(f'Error: {e}\n')