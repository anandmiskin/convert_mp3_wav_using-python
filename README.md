# convert_mp3_wav_using-python
Step 1: Their is a best library called pydub! import the AudioSegment module from pydub library from which you can manipulate audio with a simple and easy high level interface.
If you are new to pydub then run the command pip install pydub and import the library as above 

Step 2: Import os module. The OS module in Python provides functions for interacting with the operating system

Step 3: to know your current work directory their is a method .getcwd() and save the directory in the variable as directory

Step 4: os.listdir(directory) to get the list of items in that folder/directory 

Step 5: Iterate through this list of files using AudioSegment.from_mp3("song.mp3") is the method to access the song you want to convert from directory

Step 6: song.export("directory/song.wav", format="wav") is method to export it to wav format.

Note if you face error something like this :-warn("couldn't find ffprobe or avprobe - defaulting to ffprobe, but may not work", runtimewarning)  or Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work warn("Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work", RuntimeWarning) then pls follow below steps

Run this command:- conda install -c main ffmpeg 
This should work for you! 
