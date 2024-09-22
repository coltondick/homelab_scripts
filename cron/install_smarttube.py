#!/usr/bin/env python3

import os
import requests
import subprocess
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
DEVICE = os.getenv("DEVICE")  # Load DEVICE from the .env file
API_URL = "https://api.github.com/repos/yuliskov/SmartTube/releases/latest"
APK_PATH = "/tmp/smarttube_latest.apk"
LOG_FILE = "/var/log/smarttube_install.log"
LOG_MAX_SIZE = 10 * 1024 * 1024  # 10 MB

os.environ["PATH"] = "/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/local/sbin"

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)


# Log rollover function
def rollover_log():
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > LOG_MAX_SIZE:
        os.rename(LOG_FILE, f"{LOG_FILE}.old")
        logging.info(f"Log file exceeded max size. Rolled over to {LOG_FILE}.old")


# Clean up APK file
def cleanup():
    if os.path.exists(APK_PATH):
        logging.info("Cleaning up APK file.")
        os.remove(APK_PATH)


# Fetch the latest APK URL
def get_latest_apk_url():
    logging.info("Fetching latest release data from GitHub API...")
    response = requests.get(API_URL)
    release_data = response.json()

    for asset in release_data["assets"]:
        if "SmartTube_stable" in asset["name"] and "arm64-v8a.apk" in asset["name"]:
            return asset["browser_download_url"], asset["name"]
    return None, None


# Download the APK
def download_apk(apk_url):
    logging.info(f"Downloading APK from {apk_url} to {APK_PATH}")
    response = requests.get(apk_url)
    with open(APK_PATH, "wb") as apk_file:
        apk_file.write(response.content)


# Install the APK via adb
def install_apk():
    logging.info(f"Connecting to device {DEVICE}...")
    subprocess.run(["docker", "exec", "adb", "adb", "connect", DEVICE], check=True)

    logging.info(f"Installing APK on device {DEVICE}...")
    subprocess.run(
        ["docker", "exec", "adb", "adb", "-s", DEVICE, "install", "-r", APK_PATH],
        check=True,
    )


# Main function
def main():
    # Add a separator at the beginning of each execution
    logging.info("--------------------------------------------------")
    logging.info(f"Starting new execution at {datetime.now()}")

    try:
        rollover_log()

        apk_url, apk_name = get_latest_apk_url()
        if not apk_url:
            logging.error("Failed to find APK download URL.")
            return

        apk_version = apk_name.split("_")[2]
        logging.info(f"Found APK version: {apk_version}")

        download_apk(apk_url)
        install_apk()

        logging.info(f"APK version {apk_version} installed successfully!")
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        cleanup()


if __name__ == "__main__":
    main()
