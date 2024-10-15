import requests
import json
import time
import os

base_url = "https://ad.ecsc2024.it/api/scoreboard/table/"
total_rounds = 210

# Create a 'data' folder if it doesn't exist
data_folder = "data"
os.makedirs(data_folder, exist_ok=True)

for round_id in range(1, total_rounds + 1):
    url = f"{base_url}{round_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Save the data to a JSON file in the 'data' folder
        file_path = os.path.join(data_folder, f"{round_id}.json")
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        
        print(f"Successfully saved data for round {round_id}")
        
        # Add a small delay to avoid overwhelming the server
        time.sleep(1)
    
    except requests.RequestException as e:
        print(f"Error fetching data for round {round_id}: {e}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON for round {round_id}")
    except IOError:
        print(f"Error saving file for round {round_id}")

print("Data collection complete.")


