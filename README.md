# YouTube Video and Audio Downloader

This project consists of Python scripts that allow users to search for YouTube videos, download audio files from videos, or download videos with the desired resolution. The scripts utilize the `youtube-search` library for searching YouTube content and `pytube` for downloading.

## Prerequisites

- **Python**: Ensure you have Python installed (preferably version 3.6+).
- **Required Libraries**: Install the necessary Python libraries by running:
  ```bash
  pip install youtube-search pytube


## Script 1: YouTube Search

### Description

This script allows users to search for YouTube videos based on a title and either open them in a web browser or display a list of results.

### How to Use

1. Run the script:
   ```bash
   python youtube_search.py
   ```
2. Input the video's title when prompted:
   ```
   Enter the title of the video to be searched:
   ```
3. Enter the number of search results you wish to display:
   ```
   Enter the no. of results to be shown:
   ```
4. If only one result is found, the video will open in the browser.
5. If multiple results are found, choose the video by entering its index number, and it will open in your browser.

---

## Script 2: Audio Downloader

### Description

This script allows users to search for YouTube videos based on a song's title and download the audio in MP3 format.

### How to Use

1. Run the script:
   ```bash
   python audio_downloader.py
   ```
2. Input the song's title when prompted:
   ```
   Enter the title of the song to be searched:
   ```
3. Enter the number of search results you wish to display:
   ```
   Enter the no. of results to be shown:
   ```
4. Choose a song to download by entering the index number.
5. Provide the download path when prompted, and the audio will be downloaded as an MP3 file.

### Features

- Automatically converts downloaded audio to MP3 format.
- Handles errors and ensures the song is downloaded only once.

---

## Script 3: Video Downloader

### Description

This script allows users to search for YouTube videos, view the results, and choose a video to download in a specified resolution. It also gives an option to preview the video before downloading.

### How to Use

1. Run the script:
   ```bash
   python video_downloader.py
   ```
2. Input the video's title:
   ```
   Enter the title of the video to be searched:
   ```
3. Enter the number of search results you wish to display:
   ```
   Enter the no. of results to be shown:
   ```
4. Provide the desired video resolution (e.g., `720p`, `1080p`):
   ```
   Enter the desired resolution for the downloaded video:
   ```
5. Choose whether to preview the video or proceed directly to download by inputting `Y` or `N`.
6. If you proceed with the download, provide the download path.

### Features

- Downloads videos in the selected resolution.
- Option to preview the video before downloading.
- Handles errors and invalid inputs.

---

## Notes

- Ensure you have a stable internet connection while using these scripts.
- The download location must have sufficient space and write permissions.
