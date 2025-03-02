import os
import json

def main():
    with open("localization.json", "r", encoding="utf-8") as f:
        jpn_backup = json.load(f).get("jpn", {})

    localization = {"eng": {}, "jpn": {}}
    data_files = []

    for root, _, files in os.walk("data"):
        if "data.json" in files:
            path = os.path.join(root, "data.json")
            data_files.append(path)
            print(path)

    for data_file in data_files:
        with open(data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            localization["eng"].update(data)

    localization["jpn"].update(jpn_backup)

    with open("localization.json", "w", encoding="utf-8") as f:
        json.dump(localization, f, indent=4, ensure_ascii=False)

    print(f"- GENERATON COMPLETE -")

if __name__ == "__main__":
    main()
