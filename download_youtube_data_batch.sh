#!/user/bin/bash
mkdie -p ~/youtube_data
while read p; do
	python3 download_youtube_data.py $p >~/youtube_data/$p.json
done <video_ids.txt
