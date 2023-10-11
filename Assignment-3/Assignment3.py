import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Navigate to the website
driver.get("https://open.spotify.com/")
# Wait for a few seconds to let the login form appear
time.sleep(5)

# Locate and click the login button
login_button = driver.find_element(By.XPATH, "//button[@data-testid='login-button']")
login_button.click()

# Wait for a few seconds to let the login form appear
time.sleep(5)

# Locate the username and password input fields and submit the credentials
username_input = driver.find_element(By.ID, "login-username")
password_input = driver.find_element(By.ID, "login-password")

# Enter your Spotify username and password
username_input.send_keys("layadummy@gmail.com")  # Replace with your actual username
password_input.send_keys("dummy@1234")  # Replace with your actual password

# Locate and click the login button (the one inside the login form)
login_submit_button = driver.find_element(By.ID, "login-button")
login_submit_button.click()

# Wait for a few seconds to let the login process complete
time.sleep(15)

# Locate the element for Select Playlist (you can update the XPath)
Select_playlist = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/nav/div[2]/div[1]/div[2]/div[4]/div/div/div/div[2]/ul/div/div[2]/li[1]/div/div[1]")

# Create an instance of ActionChains
actions = ActionChains(driver)

# Perform a double click on the element
actions.double_click(Select_playlist).perform()

# Wait for a few seconds to let the login form appear
time.sleep(5)

# Locate and click the play button to play Music
play_button = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[4]/div/div/div/div/div/button")
play_button.click()

# Wait for a few seconds to let the login form appear
time.sleep(20)

# user settings
user_settings = driver.find_element(By.XPATH, "//button[@class='Button-sc-1dqy6lx-0 fXEXug encore-over-media-set SFgYidQmrqrFEVh65Zrg']")
user_settings.click()
time.sleep(3)

# Click Logout
logout_button = driver.find_element(By.XPATH, "//button[@data-testid='user-widget-dropdown-logout' and @class='wC9sIed7pfp47wZbmU6m']")
logout_button.click()
time.sleep(8)

login_page_check = driver.find_element(By.XPATH, "//button[@data-testid='login-button']")
time.sleep(3)

driver.quit()
