from pathlib import Path
import json

paths = [str(x) for x in Path('./youtube_data').glob('**/*.json')]

results = []
for path in paths:
    with open(path, 'r') as f:
        data = json.load(f)
    for i in data:
        
        dic = {
            'Video_id:' +i['id'],
            'Title: '+i['title'],
            'Description: '+i['discription'],
            
        }
    results.append(dic)

with open('data_for_indexing.json', 'w') as dump_file:
    json.dump(results, dump_file)
