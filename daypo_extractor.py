import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fpdf import FPDF
from PIL import Image
import os

# Path to the Chrome extension file (.crx)
extension_path = "./ad-blocker.crx"

# Chrome WebDriver service
service = Service('/usr/bin/chromedriver')  # Update with the path to your chromedriver executable

# Chrome options
options = webdriver.ChromeOptions()

# Add the extension
options.add_extension(extension_path)

# Initialize Chrome WebDriver with options and service
driver = webdriver.Chrome(service=service, options=options)

# Open the webpage
driver.get("https://en.daypo.com/cs508-lt503.html#test")

pdf = FPDF()
screenshot_directory = 'screenshots'
os.makedirs(screenshot_directory, exist_ok=True)

try:
    # Wait for the new tab to open after extension installation
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[1])

    # Close the new tab
    driver.close()

    # Switch back to the original tab
    driver.switch_to.window(driver.window_handles[0])

    # Refresh the original tab
    driver.refresh()

    for question_number in range(1, 164):  # From 1 to 163 inclusive
        # Click the "Answer" button
        answer_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "boton"))
        )
        answer_button.click()

        # Sleep for 0.3 second before processing the next question
        time.sleep(.3)

        # Wait for the question element to be visible
        question_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "pri1"))
        )

        # Screenshot the area of question and answers
        screenshot_path = f"{screenshot_directory}/screenshot_{question_number}.png"
        driver.save_screenshot(screenshot_path)
        
        # Click the "Continue" button
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "boton"))
        )
        continue_button.click()


except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser window
    driver.quit()

    # Convert screenshots to PDF
    for i in range(1, 164):  # Include all screenshots from 1 to 163
        image_path = f"{screenshot_directory}/screenshot_{i}.png"
        if os.path.exists(image_path):
            cover = Image.open(image_path)
            width, height = cover.size
            pdf.add_page()
            pdf.image(image_path, 0, 0, 210, 297 * height / width)  # Resize image to fit A4

    pdf.output("Questions_and_Answers.pdf", "F")
