#!/user/bin/bash

while read p; do
	python3 download_youtube_data.py $p 
done <video_ids.txt
