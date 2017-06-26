# Import modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

# Create and define chrome webdriver, with the headless option

chrome_options = Options()
chrome_options.add_argument("--window-size=1024x768")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)

# Define the XPATH text of the navigation elements that will be used for operating the API
# Note that these will likely change over time as Pandora updates the UI on pandora.com

loginButton = "//a[@data-qa='header_login_button']"
emailInput = "//input[@data-qa='email_input']"
passwordInput = "//input[@data-qa='password_input']"

playButton = "//button[@data-qa='play_button']"
pauseButton = "//button[@data-qa='pause_button']"
skipButton = "//button[@data-qa='skip_button']"
likeButton = "//button[@data-qa='thumbs_up_button']"
dislikeButton = "//button[@data-qa='thumbs_down_button']"

radioStations= "//a[@data-qa='header_my_stations_link']"
stationPlayButton = "//div[@data-qa='header_button_row_start_station']"
nowPlaying = "//a[@data-qa='header_now_playing_link']"

# Define login function

def Login(username="user", password = "password"):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, loginButton))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, emailInput))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, passwordInput))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, passwordInput))).submit()

    print("Login successfull!")

# Function to Play/Pause the currently selected radio

def PlaySong():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, playButton))).click()

def PauseSong():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, pauseButton))).click()

# Skip the current song

def SkipSong():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, skipButton))).click()

# Like (thumbs up) the current song

def LikeSong():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, likeButton))).click()
    
# Dislike (thumbs down) the current song

def DislikeSong():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, dislikeButton))).click()

# Get stations function

def ListStations():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, radioStations))).click()

    for i in driver.find_elements_by_class_name("SingleToggleButton__button"):
        if i.text == "A-Z":
            i.click()

    stationEls = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "MyStationsListItem__trackName")))
    stations = []

    for i in stationEls:
        stations.append(i.text)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, nowPlaying))).click()

    return stations


def PlayStation(station = "my station"):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, radioStations))).click()

    for i in driver.find_elements_by_class_name("SingleToggleButton__button"):
        if i.text == "A-Z":
            i.click()

    stationEls = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "MyStationsListItem__trackName")))

    for ndx,el in enumerate(stationEls):
        if el.text == station and ndx >= 1:
            driver.execute_script("arguments[0].scrollIntoView(true);", stationEls[ndx-1])  # needed for link click to be successfull by moving it into view
            el.click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, stationPlayButton))).click()
            break
        elif el.text == station and ndx == 0:
            el.click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, stationPlayButton))).click()
            break

# Load the pandora webpage, and log in
driver.get("http://www.pandora.com")

username = 'user@test.com'
password = 'mypassword'

# Perform initial login and play the first station in the account (alphabetically)

Login(username, password)

myStations = ListStations()
PlayStation(myStations[0])
