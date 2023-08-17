@echo off
setlocal enabledelayedexpansion

yt-dlp --list-extractors
if not exist "sites_list.txt" (
	yt-dlp --list-extractors >> sites_list.txt
) else (
	for %%F in ("sites_list.txt") do (
        if %%~zF lss 1 (
			yt-dlp --list-extractors >> sites_list.txt
		)
	)
)
pause