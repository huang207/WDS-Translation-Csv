import os
import json
import shutil

csv_header = "Id,SpeakerName,Phrase,translation"
episode_json_path = "EpisodeJson"
episode_csv_path = "EpisodeCsv"

for _, _, files in os.walk(episode_json_path):
    for file in files:
        if file.endswith(".json"):
            content = csv_header + "\n"
            with open(f'${episode_json_path}/${file}', "r", encoding="utf-8") as fp:
                episode = json.load(fp)
                for item in episode.get("EpisodeDetail", {}):
                    content = (
                        content
                        + item.get("Id")
                        + ","
                        + item.get("SpeakerName", "")
                        + ","
                        + item.get("Phrase", "")
                        + ","
                        + "\n"
                    )
            filename = file.split('.')[0]
            with open(f'${episode_csv_path}/${filename}.csv', "w", encoding="utf-8") as fp:
                fp.write(content)

shutil.rmtree(episode_json_path)