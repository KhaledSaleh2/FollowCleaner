from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up browser
driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed
driver.get("https://www.instagram.com/")

# Log in
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

my_username = '' # Enter username inside the quotes
my_password = '' # Enter password inside the quotes
username.send_keys(my_username)
password.send_keys(my_password)
password.send_keys(Keys.RETURN)

time.sleep(5)  # Wait for login

# Navigate to your profile
url = 'https://www.instagram.com/' + my_username
driver.get(url)

time.sleep(3)

# Access followers
followers_button = driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
followers_button.click()
time.sleep(3)

followers_dialog = driver.find_element(By.CSS_SELECTOR, "div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6")

# Store the initial scroll position
last_height = driver.execute_script("return arguments[0].scrollHeight", followers_dialog)
while True:
    # Scroll to the bottom of the followers dialog
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_dialog)
    time.sleep(1)  # Wait for new followers to load
    
    # Get the new scroll position
    new_height = driver.execute_script("return arguments[0].scrollHeight", followers_dialog)
    
    # If the scroll height hasn't changed, we've reached the bottom
    if new_height == last_height:
        break
    last_height = new_height


# Scrape all loaded followers
follower_usernames = driver.find_elements(By.CSS_SELECTOR, "span._ap3a._aaco._aacw._aacx._aad7._aade")

# Loop through the list of elements and print each username
i = 1
followers_set = set()

print('\nFOLLOWERS:\n')
for username in follower_usernames:
    followers_set.add(username.text)
    print(i, username.text)
    i += 1

url = 'https://www.instagram.com/' + my_username
driver.get(url)

time.sleep(3)

following_button = driver.find_element(By.PARTIAL_LINK_TEXT, "following")
following_button.click()
time.sleep(3)

following_dialog = driver.find_element(By.CSS_SELECTOR, "div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6")

# Store the initial scroll position
last_height = driver.execute_script("return arguments[0].scrollHeight", following_dialog)
following_set = set()

while True:
    # Scroll to the bottom of the following dialog
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", following_dialog)
    time.sleep(1)  # Wait for new following to load
    
    # Get the new scroll position
    new_height = driver.execute_script("return arguments[0].scrollHeight", following_dialog)
    
    # If the scroll height hasn't changed, we've reached the bottom
    if new_height == last_height:
        time.sleep(5)
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", following_dialog)
        time.sleep(1)  # Wait for new following to load
    
        # Get the new scroll position
        new_height = driver.execute_script("return arguments[0].scrollHeight", following_dialog)
        if new_height == last_height:
            break
    last_height = new_height

# Scrape all loaded following
following_usernames = driver.find_elements(By.CSS_SELECTOR, "span._ap3a._aaco._aacw._aacx._aad7._aade")
i = 1
print('\nFOLLOWING:\n')
for username in following_usernames:
    following_set.add(username.text)
    print(i, username.text)
    i += 1

# Find users to unfollow
to_unfollow = following_set - followers_set

print("\nUNFOLLOWING:\n")
i = 1
# Unfollows all accounts that don't follow you back
for username in to_unfollow:
    print(i, username)
    url = 'https://www.instagram.com/' + username
    driver.get(url)

    time.sleep(1)
    while True:
        try:
            following_button = driver.find_element(By.CSS_SELECTOR, "button._acan._acap._acat._aj1-._ap30")
            following_button.click()
            time.sleep(1)  # Wait for the action to complete

            unfollow_button = driver.find_element(By.XPATH, "//span[text()='Unfollow']")
            unfollow_button.click()
            break
        except Exception as e:
            print(f"Error unfollowing {username}: {e}")
            # Refresh the page and retry
            print(f"Retrying {username}...")
            driver.refresh()
            time.sleep(1)
    i += 1
    time.sleep(1)

# Close the browser
driver.quit()
