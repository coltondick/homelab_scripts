import os
from pyarr import RadarrAPI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Radarr API URL and API key from environment variables
api_url = os.getenv("RADARR_API_URL")
api_key = os.getenv("RADARR_API_KEY")

# Create a RadarrAPI object
radarr = RadarrAPI(host_url=api_url, api_key=api_key)


def list_movies_with_null_collection_type():
    try:
        # Fetch all movies
        movies = radarr.get_movie()

        # Iterate and find movies with null 'CollectionType'
        for movie in movies:
            if movie.get("collectionType") is None:
                print(f"Title: {movie['title']} - CollectionType is null")

    except Exception as e:
        print(f"An error occurred: {e}")


# Call the function
list_movies_with_null_collection_type()
