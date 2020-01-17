:: Create File List
for %%i in (*.wav) do echo file '%%i'>> mylist.txt

:: Concatenate Files
ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.wav