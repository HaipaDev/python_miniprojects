## Most code from https://stackoverflow.com/questions/64430805/how-to-compress-video-to-target-size-by-python ##

import subprocess
## Install ffmpeg-python if its not already installed
module_name = "ffmpeg-python"
subprocess.run(["pip", "install", module_name])

import sys, os, ffmpeg

input_filename=""
input_path=""
target_size=24
if(__name__ == "__main__"):
    if(len(sys.argv) > 1):
        input_filename = sys.argv[1]
        input_path=os.path.dirname(input_filename)
    if(len(sys.argv) > 2):
        target_size = int(sys.argv[2])

#print(input_filename)
#print(input_path)
#print("\n")

def compress_video(video_full_path, output_file_name, target_size):
    input_size = os.path.getsize(video_full_path)
    #print(f"{input_size} | {target_size*1000}")
    if input_size <= target_size * 1000:
        print("Input video is already below or at the target size. Skipping compression.\n")
        return
    else:
        if os.path.exists(output_file_name):
            print("Compressed video already exists. Replacing old file!\n")
            os.remove(output_file_name)

        # Reference: https://en.wikipedia.org/wiki/Bit_rate#Encoding_bit_rate
        min_audio_bitrate = 32000
        max_audio_bitrate = 256000

        probe = ffmpeg.probe(video_full_path)
        # Video duration, in s.
        duration = float(probe["format"]["duration"])
        # Audio bitrate, in bps.
        audio_bitrate = float(next((s for s in probe["streams"] if s["codec_type"] == "audio"), None)["bit_rate"])
        # Target total bitrate, in bps.
        target_total_bitrate = (target_size * 1024 * 8) / (1.073741824 * duration)

        # Target audio bitrate, in bps
        if 10 * audio_bitrate > target_total_bitrate:
            audio_bitrate = target_total_bitrate / 10
            if audio_bitrate < min_audio_bitrate < target_total_bitrate:
                audio_bitrate = min_audio_bitrate
            elif audio_bitrate > max_audio_bitrate:
                audio_bitrate = max_audio_bitrate
        # Target video bitrate, in bps.
        video_bitrate = target_total_bitrate - audio_bitrate

        i = ffmpeg.input(video_full_path)
        ffmpeg.output(i, os.devnull,
                    **{"c:v": "libx264", "b:v": video_bitrate, "pass": 1, "f": "mp4"}
                    ).overwrite_output().run()
        ffmpeg.output(i, output_file_name,
                    **{"c:v": "libx264", "b:v": video_bitrate, "pass": 2, "c:a": "aac", "b:a": audio_bitrate}
                    ).overwrite_output().run()

# Compress input.mp4 to 24MB and save as output.mp4
#print(input_filename)
compress_video(f"{input_filename}", f"{input_filename.split('.mp4')[0]}_comp.mp4", target_size * 1000)

# Remove the temp files created from the process
os.remove(f"ffmpeg2pass-0.log.mbtree")
os.remove(f"ffmpeg2pass-0.log")
os.remove((f"{input_path}//ffmpeg2pass-0.log.mbtree").replace("//","\\"))
os.remove((f"{input_path}//ffmpeg2pass-0.log").replace("//","\\"))