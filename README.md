# FollowCleaner
This repository contains a script that can be used to unfollow every instagram user that does not follow you back (non-mutuals). 

# How to Use:
**Step 1: Enter your login info**
Insert your instagram username and password inside the quotes where the variables 'my_username' and 'my_password' are defined. Additionally, make sure the script is being ran on a computer that has been used to sign into your instagram before. This will make it so additional security codes are not necessary to login. Furthermore, make sure multi-factor authentication is turned off on your account

**Step 2: Open a virtual environment**
Head to your terminal and open a virtual environment in the same folder where you have this script downloaded. If you are unsure how to do this, check out this [website](https://python.land/virtual-environments/virtualenv) (it is very simple). Inside the virtual environment, run commands 'pip install selenium' and 'pip install chromedriver-autoinstaller'. 

**Step 3: Run the Script**
From here, you should be able to run the script from terminal using 'python unfollow_non-mutuals.py'.

**Disclaimer**
The script does take some time to run, and if you have thousands of followers/following, it could take upwards of 30 minutes to an hour. I recommend running the script while you occupy yourself with some other task. Also, the script will unfollow ALL accounts that do not follow you back, including celebrities, media sources, organizations, etc. If there are certain major accounts that you do not wish to unfollow, I suggest writing them down before running the script so you can refollow them afterwards.
