# FollowCleaner (Instagram)

**FollowCleaner** is a Python script designed to automatically unfollow Instagram accounts that do not follow you back (non-mutuals). 

## How to Use

### Step 1: Enter Your Login Information
- Update the `my_username` and `my_password` variables in the script with your Instagram username and password. 
- Ensure that the script is run on a device previously used to log into your Instagram account to avoid additional security checks.
- Make sure multi-factor authentication (MFA) is disabled for your account before running the script.

### Step 2: Set Up a Virtual Environment
- Open a terminal and create a virtual environment in the folder where this script is located. [Learn how to set up a virtual environment.](https://python.land/virtual-environments/virtualenv)
- Inside the virtual environment, install the required dependencies:
  ```bash
  pip install selenium
  pip install chromedriver-autoinstaller

### Step 3: Run the Script
- Execute the script in your terminal:
  ```bash
  python unfollow_non_mutuals.py

## Disclaimer
- **Runtime**:  
  The script may take considerable time to complete, especially for accounts with thousands of followers or followings (up to 30 minutes or more). 

- **Important Accounts**:  
  The script will unfollow **all non-mutuals**, including public figures, organizations, or media accounts. If you want to retain specific accounts, make a list and refollow them manually after running the script.
