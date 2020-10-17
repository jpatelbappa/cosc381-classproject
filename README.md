# cosc381-classproject
Part1: Requirements.txt added

Part2: Google Search Data
    -first update the config.py file 
    -run se.py file

Part3: Youtube data
    -run program as:
        -to get the video_ids from google_search.txt
        $ grep "'link'" google_search.txt | awk -F '=' '{print substr($2,1,11)}'
        -to get the result for one video_id :
        $ python3 download_youtube_data.py <video_id>
        -to get results for all video_ids :
        $ bash download_youtube_data_batch.sh
    - in youtube_data.txt you will find results for all video_ids
    - video_ids.txt contains all the video_ids from google_search

Part4: prepare data for whoosh indexing
    -first update the file download_youtube_data.py(use the following code to run the file)
    -updated download_youtube_data.py
import pprint
import sys
import config
import json
from googleapiclient.discovery import build
my_api_key = config.api_key

def youtube_data(video_id):
    service = build("youtube", "v3", developerKey=my_api_key)
    result = service.videos().list(part='snippet', id=video_id).execute()
    return result

if __name__ == '__main__':
    result = youtube_data(sys.argv[1])
    pprint.pprint(result)

with open (sys.argv[1]+'.json','w') as dump_file:
    json.dump(result, dump_file)


-same way update the download_yotube_data_batch.sh
    #!/user/bin/bash
mkdir -p ~/youtube_data
while read p; do
	python3 download_youtube_data.py $p > ~youtube_data/$p.json
done <video_ids.txt

- then run bash download_youtube_data_batch.sh
- then run create_data_for_indexing.py




Part5: To create a whoosh index
    - run create_whoosh_index.py file to create "indexdir"

Part6: search On whoosh index
    -run query_on whoosh.py file

Part7: .gitignore is made 

        
