Code by HyperGamesDev | https://hypergamesdev.github.io | https://hyperr.carrd.co
The whole program requires Python which you an get at: https://www.python.org/downloads/
This script requires ffmpeg installed as well as obviously yt-dlp
You can download yt-dlp on GitHub at: https://github.com/yt-dlp/
And FFMPEG at: https://ffmpeg.org/download.html
Or you can autoinstall everything by running install_python.bat and install_ffmpeg.bat

By putting urls line by line in the inputurls.txt file they will succesively export automatically
And as it is said in the program you can put a timestamp for a snippet
formatted after the url like *01:03-01:37

The downloader does work with *a lot of* different sites, but probably best with YouTube, including the timestamps, they work weird with for ex. TikTok, it glitches out
You can run check_sites.bat to see which sites does it support

DO NOT run run_downloads.bat by itself
Thats what other bat files are made for with a predetermined extension