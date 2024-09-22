import os
from pyarr import RadarrAPI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Radarr API URL and API key from environment variables
host_url = os.getenv("RADARR_API_URL")
api_key = os.getenv("RADARR_API_KEY")

# Initialize the API
radarr = RadarrAPI(host_url, api_key)

# Get the queue
queue_data = radarr.get_queue()
print("Queue Data Type:", type(queue_data))
print("Queue Data:", queue_data)

# Assuming queue_data is a dictionary, and the actual queue is under a key
queue = queue_data.get("records", [])  # Adjust the key based on actual structure

for item in queue:
    print("Item Type:", type(item))
    print("Item:", item)
    if not item.get("downloaded"):  # Use get to avoid KeyError
        movie_id = item["movieId"]  # Adjust key names as necessary
        # Remove from queue and blocklist
        radarr.remove_from_queue(movie_id, blocklist=True)
