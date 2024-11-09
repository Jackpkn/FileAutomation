# 🗂️ Downloads Folder Organizer

Ever looked at your Downloads folder and thought "what a mess"? Same. That's why I built this - a Python script that automatically organizes files as they land in your Downloads folder.

## ✨ What it does

This script is like having a neat freak friend who:
- Watches your Downloads folder 24/7
- Instantly sorts files into the right folders based on their type
- Handles duplicate files without breaking a sweat
- Keeps a log of what's moved where

## 🗄️ File Organization Structure

Files get sorted like this:
```
~/Downloads       -> Source directory
~/Pictures       -> Images (.jpg, .jpeg, .png, .gif, etc.)
~/Videos         -> Videos (.mp4, .avi, .mov, etc.)
~/Music         -> Music files (.mp3, .wav, .flac)
~/Downloads/SFX  -> Small audio files (< 10MB)
~/Documents     -> Documents (.pdf, .docx, .xlsx, etc.)
~/GitHub        -> Git repositories
```

## 🛠️ Setup and Usage

1. Make sure you have Python installed
2. Install required packages:
   ```bash
   pip install watchdog
   ```
3. Clone this repo:
   ```bash
   git clone [your-repo-url]
   ```
4. Update the directory paths in the script to match your system
5. Run it:
   ```bash
   python organizer.py
   ```

## 🔧 Under the Hood

Here's how it works:

![Architecture Diagram](link-to-your-diagram)

The script uses Watchdog to monitor file system events and automatically moves files to appropriate directories based on their extensions. It includes smart handling for:
- Duplicate files (adds numbers to filenames)
- Special case for SFX vs Music files based on size
- Git repositories

## 🎯 Features

- Real-time file monitoring and sorting
- Smart duplicate file handling
- Separate handling for large and small audio files
- Logging of all file movements
- Handles interrupted transfers gracefully

## 📝 Requirements
- Python 3.x
- watchdog library

## ⚠️ Heads Up!
- Make sure you have all the destination folders created
- Double-check the paths before running
- The script keeps running until you stop it (Ctrl+C)

## 🤝 Contributing

Found a bug? Want to add more features? PRs are welcome! 

## 📜 License

Feel free to use this however you want!

---
Made with ☕ and a messy Downloads folder
