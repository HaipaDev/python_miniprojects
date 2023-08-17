import subprocess
## Install ffmpeg-python if its not already installed
module_name = "ffmpeg-python"
subprocess.run(["pip", "install", module_name])

import sys, os, ffmpeg

input_filename=""
input_path=""
if(__name__ == "__main__"):
    if(len(sys.argv) > 1):
        input_filename = sys.argv[1]
        input_path=os.path.dirname(input_filename)

#print(input_filename)
#print(input_path)
#print("\n")

def mute_video(video_full_path, output_file_name):
    if os.path.exists(output_file_name):
        print("Muted video already exists.\n")
        return
        #os.remove(output_file_name)

    # Define input and output streams
    input_stream = ffmpeg.input(video_full_path)
    output_stream = ffmpeg.output(input_stream['v'], output_file_name, acodec='copy', vcodec='copy', format='mp4')

    # Run the ffmpeg command
    ffmpeg.run(output_stream)

mute_video(f"{input_filename}", f"{input_filename.split('.mp4')[0]}_muted.mp4")