from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the website
driver.get("https://www.google.com")

# Wait for a few seconds to let the page load
time.sleep(3)

# Take a screenshot
driver.save_screenshot("screenshot.png")

# Close the browser
driver.quit()

print("Screenshot saved!")
