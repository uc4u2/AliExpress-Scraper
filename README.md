# AliExpress-Scraper

_A beginner-friendly tool to extract and analyze winning products from AliExpress using Python and PowerShell._

## Table of Contents

- [Introduction](#introduction)
- [System Requirements](#system-requirements)
- [Getting Started](#getting-started)
  - [Project Structure](#project-structure)
  - [Setting Up the Environment](#setting-up-the-environment)
  - [Installing Dependencies](#installing-dependencies)
- [Usage](#usage)
  - [Running the Scraper Manually](#running-the-scraper-manually)
  - [Scheduling the Scraper with PowerShell](#scheduling-the-scraper-with-powershell)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [Contact](#contact)

---

## Introduction

Product research is critical for identifying profitable products in the competitive e-commerce market. **AliExpress-Scraper** automates the process by fetching product data from AliExpress (via RapidAPI), filtering it based on key criteria (minimum orders, rating, and maximum price), and exporting the results to an Excel file. This tool is designed for beginners—no UI or advanced programming needed. Simply run the script using Windows PowerShell to get your Excel report.

---

## System Requirements

- **Operating System:** Windows 10 or later
- **Software:**
  - Python (latest version recommended)
  - Microsoft Excel (or a free alternative like LibreOffice Calc)
  - Windows PowerShell (pre-installed on Windows)
- **Internet Connection:** Required to fetch data from the AliExpress API

---

## Getting Started

### Project Structure

Your project folder should look like this:
C:\Aliscraper └── backend ├── scraper.py ├── RunScraper.ps1 └── README.md




### Setting Up the Environment

1. **Create Project Folders:**
   - Create a folder named `Aliscraper` on your C: drive.
   - Inside, create a subfolder named `backend`.

2. **Set Up a Python Virtual Environment:**
   - Open Windows PowerShell and navigate to the backend folder:
     ```powershell
     cd C:\Aliscraper\backend
     ```
   - Create a virtual environment:
     ```powershell
     python -m venv venv
     ```
   - Activate the virtual environment:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
     Your prompt should now show `(venv)`.

### Installing Dependencies

With the virtual environment activated, install the required libraries:
```powershell
pip install flask requests pandas flask-cors openpyxl

Note: Although Flask and flask-cors are installed for potential future expansion, this project uses Python and PowerShell only.

Usage
Running the Scraper Manually
Open Windows PowerShell.
Navigate to the backend folder:
powershell

cd C:\Aliscraper\backend
Activate the Virtual Environment:
powershell

.\venv\Scripts\Activate.ps1
Run the Python Script:
powershell

python scraper.py
Check the Output:
The script logs messages in PowerShell and creates an Excel file named winning_products.xlsx in the backend folder.
Scheduling the Scraper with PowerShell
Create a PowerShell Script File:
Save the following content as RunScraper.ps1 in your C:\Aliscraper\backend folder:
powershell

cd C:\Aliscraper\backend
.\venv\Scripts\Activate.ps1
python scraper.py
Schedule the Task Using Windows Task Scheduler:
Press Win + R, type taskschd.msc, and press Enter.
Click Create Basic Task… and follow these steps:
Name: "Run AliExpress Scraper"
Trigger: Set your desired schedule (e.g., daily or every few hours).
Action: "Start a Program"
Program/Script: powershell.exe
Add Arguments:
powershell

-ExecutionPolicy Bypass -File "C:\Aliscraper\backend\RunScraper.ps1"
Finish and save the task. The scraper will run automatically according to the schedule.
How It Works
The AliExpress-Scraper script follows these steps:

Data Extraction:

Uses the RapidAPI endpoint for AliExpress to fetch product data for multiple search queries.
Iterates through pages and collects product details such as name, price, orders, and rating.
Data Filtering:

Applies winning criteria:
Minimum orders: 5
Minimum rating: 4
Maximum price: $30.0
Sorts the filtered (winning) products in descending order by the number of orders.
Data Export:

Converts the filtered product list into an Excel file (winning_products.xlsx) using Pandas and openpyxl.
Troubleshooting
API Errors:
Verify that your API key is correct.
Check that you are within the allowed rate limits.
Python Errors:
Ensure all required libraries are installed.
Make sure your virtual environment is activated.
PowerShell Issues:
Confirm that the paths in your scripts are correct.
Ensure you are running PowerShell with the appropriate execution policy.
License

Contact
For any questions or assistance, please contact:
photoartisto.ca@gmail.com

PowerShell Command Summary
powershell

# Verify Python Installation:
python --version

# Navigate to Backend Folder:
cd C:\Aliscraper\backend

# Create & Activate Virtual Environment:
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install Dependencies:
pip install flask requests pandas flask-cors openpyxl

# Run the Python Script:
python scraper.py

# Optional – Create a PowerShell Script (RunScraper.ps1):
cd C:\Aliscraper\backend
.\venv\Scripts\Activate.ps1
python scraper.py

# Schedule Task in Windows Task Scheduler:
# Program: powershell.exe
# Arguments: -ExecutionPolicy Bypass -File "C:\Aliscraper\backend\RunScraper.ps1"
