import requests
import json
from tqdm import tqdm

API_KEY = "m87W6pSKYjoGuU59BsUOQuwwvVJHG8We"
INDEX_NAME = "RIN_Tool_pr"
BASE_URL = f"https://api.scicrunch.io/elastic/v1/{INDEX_NAME}"
SCROLL_URL = "https://api.scicrunch.io/elastic/v1/_search/scroll"
HEADERS = {
    "Content-Type": "application/json",
    "apikey": API_KEY
}

def fetch_all_records():
    all_records = []
    total_records = 0

    payload = {
        "size": 1000,  # Number of results per request
        "query": {"match_all": {}}
    }
    response = requests.post(f"{BASE_URL}/_search?scroll=1m", headers=HEADERS, json=payload)

    if response.status_code != 200:
        print("Error:", response.text)
        return

    data = response.json()
    scroll_id = data.get("_scroll_id")
    hits = data["hits"]["hits"]
    total_records += len(hits)

    if not scroll_id or not hits:
        print("No data returned.")
        return

    all_records.extend(hits)
    print(f"Fetched {total_records} records...")

    with tqdm(desc="Downloading Data", unit=" records") as pbar:
        while hits:
            payload = {
                "scroll": "1m",
                "scroll_id": scroll_id
            }
            response = requests.post(SCROLL_URL, headers=HEADERS, json=payload)
            
            if response.status_code != 200:
                print("Error:", response.text)
                break

            data = response.json()
            scroll_id = data.get("_scroll_id")
            hits = data["hits"]["hits"]

            if not hits:
                print("No more records to fetch.")
                break

            all_records.extend(hits)
            total_records += len(hits)
            pbar.update(len(hits))  # Update progress bar

    # Step 3: Save Data to JSON File
    with open("rin_data.json", "w") as f:
        json.dump(all_records, f, indent=4)

    print(f"\nDownload complete! {total_records} ")

if __name__ == "__main__":
    fetch_all_records()
