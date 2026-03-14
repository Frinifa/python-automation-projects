# Python Automation Projects

A collection of simple Python scripts for common automation tasks.

## Description

This repository contains Python automation scripts designed to perform basic file operations, text analysis, password generation, and web scraping. These scripts are lightweight, easy to use, and demonstrate fundamental Python programming concepts.

## Scripts

### File Renamer (`file_renamer.py`)
- Automatically renames all files in the current directory.
- Converts files to a standardized naming format: `photo1.jpg`, `photo2.jpg`, etc.
- Useful for organizing photo collections or batch renaming files.

### Word Counter (`word_counter.py`)
- Counts words and characters in user-input text.
- Provides instant feedback on text statistics.
- Simple command-line interface for text analysis.

### Password Generator (`password_generator.py`)
- Generates a secure password with a mix of letters, numbers, and symbols.
- Allows specifying length and character set.
- Useful for creating strong passwords for accounts or services.

### Web Scraper (`web_scraper.py`)
- Scrapes the top headlines from Hacker News.
- Displays the top 10 current stories.
- Demonstrates basic web scraping with requests and BeautifulSoup.

## Requirements

- Python 3.x
- Standard library modules (os, sys, random, string)
- External libraries: requests, beautifulsoup4

## Installation

1. Clone or download the repository
2. Ensure Python 3.x is installed on your system
3. Install required dependencies: `pip install requests beautifulsoup4`

## Usage

### File Renamer
```bash
python file_renamer.py
```
Run this script in the directory containing the files you want to rename. All files will be renamed to `photo1.jpg`, `photo2.jpg`, etc.

**Warning:** This script will rename ALL files in the current directory. Make sure you're in the correct directory and have backups if needed.

### Word Counter
```bash
python word_counter.py
```
Enter a sentence when prompted. The script will display the word count and character count.

Example:
```
Enter a sentence: Hello world, this is a test.
Words: 6
Characters: 27
```

### Password Generator
```bash
python password_generator.py
```
Follow the prompts to specify the desired password length (e.g., 12). The script will output a randomly generated password.

### Web Scraper
```bash
python web_scraper.py
```
This script fetches and displays the top 10 headlines from Hacker News. Requires an internet connection.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

These scripts are provided as-is for educational and demonstration purposes. Always test scripts in a safe environment before using on important files.