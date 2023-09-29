from youtube_search import YoutubeSearch
from pytube import YouTube
import webbrowser

search=input('\nEnter the title of the video to be searched:'); print('')
result_count=int(input('Enter the no. of results to be shown:')); print('')

print('Choose a valid result count !') or quit() if result_count<1 else None

yt_search=YoutubeSearch(search, max_results=result_count).to_dict()

if result_count==1:
    webbrowser.open(f"https://www.youtube.com/{yt_search[0]['url_suffix']}")

else:
    for result in range(result_count):
        print(f'{result+1}.', f"{yt_search[result]['title']} BY {yt_search[result]['channel']}")

    choice=int(input('Enter the index no. of the video to be played:'))
    webbrowser.open(f"https://www.youtube.com/{yt_search[choice-1]['url_suffix']}")