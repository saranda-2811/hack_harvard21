Setup:
1. youtube-dl - A python library to download youtube videos
2. click - a python library
3. ffmpeg - an open source software for handling multimedia files

Go to https://ffbinaries.com/downloads and download the binaries ffmpeg, ffprobe, and ffplay. Unzip them and put them into a folder and put it in the same directory as your project.

4. Assembly AI API key - go to configure.py and enter your auth key
5. There are separate functions for downloading, uploading, etc. but to just transcribe a video from link, type in terminal - python cli.py transcribe-from-link "link"


(NOTE: The Twilio API converts all incoming messages to lowercase, hence making it invalid, so the Assembly AI API can't work with it.
Running the transcription from the terminal works just fine though.
Have created a batch file to automate the whole python scripts, so the user doesn't have to type in any command from the terminal, for easier use.)

Improvements: 
Adding summaries of the transcripts produced, adding clickable timestamps. Making more functionalities, to make the bot more useful for all. 
