import os
from pyarr import SonarrAPI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Sonarr API URL and API key from environment variables
api_url = os.getenv("SONARR_API_URL")
api_key = os.getenv("SONARR_API_KEY")

# Create a SonarrAPI object
sonarr = SonarrAPI(host_url=api_url, api_key=api_key)


def get_series_with_null_first_aired_or_overview():
    try:
        # Fetch all series
        series_list = sonarr.get_series()

        # Iterate and find series with null 'firstAired' or 'overview'
        for series in series_list:
            if series.get("firstAired") is None or series.get("overview") is None:
                print(
                    f"Title: {series['title']} - firstAired: {series.get('firstAired')} - Overview: {series.get('overview')}"
                )

    except Exception as e:
        print(f"An error occurred: {e}")


# Call the function
get_series_with_null_first_aired_or_overview()
