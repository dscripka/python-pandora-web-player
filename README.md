# python-pandora-web-player
Simple API for the Pandora web player using Selenium and the new headless mode in the latest version of Chrome/ChromeDriver. Only basic functions are implemented (login, play/pause, list stations, play a station, etc.). Performance is acceptable, but a bit slow, as the full web-page needs to be rendered by Selenium and ChromeDriver.

# Installation

Requirements are the Python bindings for Selenium (`pip install selenium`), and the latest version of the ChromeDriver binary. Installation of both of these can be found in more detail [here](https://selenium-python.readthedocs.io/installation.html).

# Usage

A basic example:
 
```
driver.get("http://www.pandora.com")

username = 'user@test.com'
password = 'mypassword'

# Perform initial login and play the first station in the account (alphabetically)

Login(username, password)

myStations = ListStations()
PlayStation(myStations[0])

```
