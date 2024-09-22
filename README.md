# Script Repository

This repository contains various scripts organized into different directories, each serving a distinct purpose. Some scripts are set up to run as cron jobs, while others are executed manually as needed.

## Table of Contents

- [Cron Jobs](#cron-jobs)
- [Media Management](#media-management)
- [RedDiscordBot](#reddiscordbot)
- [Installation Instructions](#installation-instructions)

## Cron Jobs

The `cron` directory contains scripts that are set up as cron jobs to automate tasks.

### Scripts:

- **install_smarttube.py**  
  Installs SmartTube for enhanced YouTube experience on supported devices.
- **install_smarttube.sh**  
  Shell script that automates the installation of SmartTube. This is likely used as a cron job to ensure SmartTube is installed or updated periodically.

### Execution:

All cron scripts are automatically executed according to their configured schedules. To check or modify these schedules, view the crontab file:

```bash
crontab -e
```

Example crontab entry for `install_smarttube.sh`:

```bash
0 2 * * * /docker/scripts/cron/install_smarttube.sh
```

## Media Management

This directory contains scripts to manage media files and metadata in Radarr and Sonarr.

### Scripts:

- **find_collectionType_radarr.py**  
  Queries Radarr to find collections of movies based on type. Useful for organizing or filtering collections in your movie database.

- **find_missing_airdate_sonarr.py**  
  Looks for TV shows in Sonarr that are missing air dates, helping to identify incomplete or erroneous entries in your TV show database.

- **remove_failed_imports_radarr.py**  
  Removes entries from Radarr that failed to import correctly, helping to clean up your media library and prevent clutter.

### Execution:

To execute any of these scripts, ensure the necessary environment variables are configured, then run the Python scripts:

```bash
python3 script_name.py
```

## RedDiscordBot

This directory contains a script for resetting word counts in a Discord bot.

### Script:

- **reset_word_count.py**  
  Resets word counts for users in a Discord bot. This is li used for managing a word count leaderboard in a Discord server.

### Instructions:

1. **Set up the SQLite Database**:  
   Ensure that you have a SQLite database with a table `member_words` that has the following fields:

   - `user_id`: The ID of the user.
   - `word`: The word whose count needs to be reset.
   - `quantity`: The count of the word.

2. **Usage**:  
   Run the script by passing the user ID and the word to reset as arguments.

   Example:

   ```bash
   python3 reset_word_count.py <user_id> "<word>"
   ```

   Replace `<user_id>` with the actual user ID and `<word>` with the word to reset.

   Example:

   ```bash
   python3 reset_word_count.py 12345 "example"
   ```

## Installation Instructions

### Environment Variables

Some directories may require environment variables. Ensure these are properly configured before running the scripts.

### Installing Dependencies

Make sure to install the necessary Python dependencies by using `pip` and a `requirements.txt` file (if provided). For example:

```bash
pip install -r requirements.txt
```

### Running Scripts

Scripts can be executed manually as described above. For cron job scripts, the scheduling is handled automatically by cron. To verify or modify the cron jobs, use:

```bash
crontab -e
```

## License

This project is licensed under the MIT License.
