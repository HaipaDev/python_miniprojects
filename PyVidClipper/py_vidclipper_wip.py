## Most code from https://github.com/CodingWith-Adam/trim-videos-with-ffmpeg-python ##

import subprocess
## Install ffmpeg-python if its not already installed
module_name = "ffmpeg-python"
subprocess.run(["pip", "install", module_name])

import sys, os, ffmpeg
from tkinter import PROJECTING

input_filename=""
input_path=""
start_timestamp=0
end_timestamp=10
if(__name__ == "__main__"):
    if(len(sys.argv) > 1):
        input_filename = sys.argv[1]
        input_path=os.path.dirname(input_filename)

def ask_start():
    global start_timestamp
    startMessage=""
    while((":" not in startMessage) and (not startMessage.isnumeric())):
        startMessage=input("Start timestamp (either in seconds as in 100 or formatted 1:40) ")
    
    if(":" in startMessage):
        startMessageSplit=startMessage.split(":")
        minutes=int(startMessageSplit[0])
        seconds=int(startMessageSplit[1])
        start_timestamp=(minutes*60)+seconds
        # For hours
        if(startMessage.count(":")==2):
            hours=int(startMessageSplit[0])
            minutes=int(startMessageSplit[1])
            seconds=int(startMessageSplit[2])
            start_timestamp=(hours*3600)+(minutes*60)+seconds
        elif(startMessage.count(":")>2):
            ask_start()
    else:
        start_timestamp=int(startMessage)

def ask_end():
    global end_timestamp
    endMessage=""
    while((":" not in endMessage) and (not endMessage.isnumeric())):
        endMessage=input("End timestamp (either in seconds as in 140 or formatted 2:20) ")
    
    if(":" in endMessage):
        endMessageSplit=endMessage.split(":")
        minutes=int(endMessageSplit[0])
        seconds=int(endMessageSplit[1])
        end_timestamp=(minutes*60)+seconds
        # For hours
        if(endMessage.count(":")==2):
            hours=int(endMessageSplit[0])
            minutes=int(endMessageSplit[1])
            seconds=int(endMessageSplit[2])
            end_timestamp=(hours*3600)+(minutes*60)+seconds
        elif(endMessage.count(":")>2):
            ask_end()
    else:
        end_timestamp=int(endMessage)

    

def trim(in_file, out_file, start, end):
    # Add an additional id to the end if file already exists
    exists_id = 1
    base_name, extension = os.path.splitext(out_file)
    while os.path.exists(out_file):
        out_file = f"{base_name}_{exists_id}{extension}"
        exists_id += 1

    # in_file_probe_result = ffmpeg.probe(in_file)
    # in_file_duration = in_file_probe_result.get(
    #     "format", {}).get("duration", None)
    # print(in_file_duration)
    
    input_stream = ffmpeg.input(in_file)

    video = input_stream.video.trim(start=start, end=end).setpts("PTS-STARTPTS")

    audio_streams = []
    for audio_stream in input_stream.audio:
        audio = audio_stream.filter_("atrim", start=start, end=end).filter_("asetpts", "PTS-STARTPTS")
        audio_streams.append(audio)

    combined_audio = ffmpeg.concat(*audio_streams, v=0, a=1)
    output = ffmpeg.output(video, combined_audio, out_file, format="mp4")

    output.run()

    # out_file_probe_result = ffmpeg.probe(out_file)
    # out_file_duration = out_file_probe_result.get(
    #     "format", {}).get("duration", None)
    # print(out_file_duration)


ask_start()
ask_end()
trim(f"{input_filename}", f"{input_filename.split('.mp4')[0]}_cut.mp4", start_timestamp, end_timestamp)